var socket = 0;
var r = {};
function connect() {
 if (socket != 0 && socket.readyState != 1)
  return;

 socket = io.connect("http://localhost:8787");
}

connect();

chrome.runtime.onConnect.addListener(function(port) {
  port.onMessage.addListener(function(Message) {
    /*
      requiest id
      Type : Request
    */

    var url = Message.Details.url,
        ri = Message.Details.requestId,
        type_filters = ['image', 'script', 'stylesheet', 'font'];

      for (i in type_filters) {
        if (Message.Details.type == type_filters[i]) {
          return false;
        }
      }

    if (url.startsWith("http://localhost:8787") || url.startsWith('chrome')) return;

    if (!r.hasOwnProperty(ri)) {
      r[ri] = {};
    }

    if (Message.Type == 'Complete' || Message.Type == 'ErrorOccurred') {

    } else if (Message.Type == 'Request') {
      r[ri].url = url;
      r[ri].method = Message.Details.method;
      r[ri].type = Message.Details.type;
      r[ri].requestBody = Message.Details.requestBody;
    } else if (Message.Type == 'SendHeaders') {
      try {
        r[ri].requestHeaders = Message.Details.requestHeaders;
      } catch (e) {
        r[ri].requestHeaders = [];
      }
    } else if (Message.Type == 'Received') {
      try {
        r[ri].responseHeaders = Message.Details.responseHeaders;
      } catch (e) {
        r[ri].responseHeaders = [];
      }
    } else if (Message.Type == 'Body') {
      r[ri].status_code = Message.Details.statusCode;
    }

    if (r[ri].hasOwnProperty('status_code') &&
        r[ri].hasOwnProperty('responseHeaders') &&
        r[ri].hasOwnProperty('requestHeaders') &&
        r[ri].hasOwnProperty('type') &&
        r[ri].hasOwnProperty('requestBody') &&
        r[ri].hasOwnProperty('method') &&
        r[ri].hasOwnProperty('url')) {
          console.log(r[ri]);
          socket.emit("request", JSON.stringify(r[ri]));
          delete r[ri];
    }

  });
});
