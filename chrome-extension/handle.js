var socket = 0;
function connect() {
 if (socket != 0 && socket.readyState != 1)
  return;

 socket = new WebSocket('ws://localhost:8765');
 socket.onopen = function() {
 };
 socket.onerror = function(error) {
  console.log('socket error');
  console.log(error);
 };
 socket.onmessage = function(event) {
  handleMessage(event.data);
 };
 socket.onclose = function() {
 };

}

function handleMessage(data) {
  console.log("-> "+data);
}

connect();

chrome.runtime.onConnect.addListener(function(port) {
  port.onMessage.addListener(function(Message) {
    /*
      requiest id
    */

    if (Message.Type == "SendHeaders" || Message.Type == "Completed") {
      var url = Message.Details.url;
      var method = Message.Details.method;

      if (url.indexOf('?') != -1) {
        var msg = method + ' ' + url;
        // document.getElementById('log').innerHTML += msg + '<br />';
        socket.send(JSON.stringify(Message));
      }
    }
  });
});

document.getElementById('clear').addEventListener("click", function clear() {
  document.getElementById('log').innerHTML = '';
});
