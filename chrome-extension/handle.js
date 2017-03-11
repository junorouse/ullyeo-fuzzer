var socket = 0;
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
    var url = Message.Details.url;
    var method = Message.Details.method;

    if (url.startsWith("http://localhost:8787")) return;

    var msg = method + ' ' + url;
    // document.getElementById('log').innerHTML += msg + '<br />';
    // socket.send(JSON.stringify(Message));
    socket.emit("request", JSON.stringify(Message));
  });
});

document.getElementById('clear').addEventListener("click", function clear() {
  document.getElementById('log').innerHTML = '';
});
