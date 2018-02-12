function sendText(){
var closeBtn = document.getElementById('close');
var socketStatus = document.getElementById('status');
var exampleSocket = new WebSocket("wss://ws.coinapi.io/v1/");
var msg = {
  "type": "hello",
  "apikey": "3DB1CE61-AB4D-42C9-A68B-09021B53C419",
  "heartbeat": "true",
  "subscribe_data_type": ["trade"]
}
exampleSocket.onopen = function (event) {
  exampleSocket.send(JSON.stringify(msg))
  socketStatus.innerHTML = 'Fetching results';
  socketStatus.className = 'open';
}
exampleSocket.onmessage = function (event) {
  var msg = JSON.parse(event.data);
  var symbol = msg.symbol_id;
  var n = symbol.indexOf("_");
  var n1 = symbol.indexOf("_", n + 1);
  var n2 = symbol.indexOf("_", n1 + 1);
  var price = msg.price;
  var size = msg.size;
  var buysell = msg.taker_side;
  var maxTableSize = 20;
	var length = $('table tr').length;
  if (buysell == 'BUY'){
    var bsclass= "table-success"
    }
  else {
    var bsclass= "table-danger"
  }
  $('#trades').prepend(
    "<tr class="+bsclass+"><th>" + symbol.slice(0,n)+
    "</th><th>"+ symbol.slice(n+1,n1) +
    "</th><th>"+ symbol.slice(n1+1,n2) +
    "</th><th>"+ symbol.slice(n2+1) +
    "</th><th>"+ price +
    "</th><th>"+ size +
    "</th><th>"+ buysell +
    "</th></tr>"
  );
  if (length >= (maxTableSize)) {
		$('table tr:last').remove();
	}

};

exampleSocket.onclose = function(event) {
    socketStatus.innerHTML = 'Disconnected from WebSocket.';
    socketStatus.className = 'closed';
  };
    closeBtn.onclick = function(event) {
    event.preventDefault();

    // Close the WebSocket.
    exampleSocket.close();

    return false;
  };
}


