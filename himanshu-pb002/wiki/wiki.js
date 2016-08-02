console.log("Result will be written in message.txt")
if (process. argv. length <= 2) {
	start();
}else{
	var x = process. argv[2];
	if (x=="-h") {
		console.log("1st command argument should be keyword eg node.wiki.js game")
		return 1;
	}
apicall(process. argv[2]);
}

function start(){
		var prompt = require('prompt');

  prompt.start();

  prompt.get(['keyword'], function (err, result) {
    if (err) { return onErr(err); }
    console.log('Command-line input received:');
    console.log('url for article')
     apicall(result.keyword);
  });
}

 
  function onErr(err) {
    console.log(err);
    return 1;
  }

 function apicall(word) {
  var request = require('request');
var fs = require('fs');
request({
    url: 'https://en.wikipedia.org/w/api.php?action=opensearch&search='+word,
    json: true
}, function (error, response, body) {
    if (!error && response.statusCode == 200) {
    	//var x = JSON.stringify(response.body)
        console.log(response.body[3][0]); // Show the HTML for the Modulus homepage.
        fs.appendFile('message.txt', response.body[3][0], function (err) {

});
        //console.log(response.statusCode)
    }
});
}
