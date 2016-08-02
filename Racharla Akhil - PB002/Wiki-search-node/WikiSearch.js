start()

function start() {
	var prompt = require('prompt')
	if (process.argv.length <= 2) {
		prompt.get(['keyword', 'fileName'], function (err, result) {
	     	var keyword = result.keyword
	     	var fileName = result.fileName
	     	saveURL(keyword, fileName)
	 	})
	} else if (process.argv.length == 3) {
		prompt.get(['keyword'], function (err, result) {
	     	var keyword = result.keyword
	     	saveURL(keyword, process.argv[2])
	 	})
	} else {
			saveURL(process.argv[3], process.argv[2])
	}
}

function saveURL(keyword, fileName) {
	if (keyword.length > 0 && fileName.length > 0) {
		createAndSendResponse(keyword, fileName)
	}
}

function createAndSendResponse(keyword, fileName) {
	var request = require('request')
	var fs = require('fs')
	request({
		url: 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + keyword,
		json: true
	}, function (error, response, body) {
		if (!error && response.statusCode == 200 && response.body.length >= 4 && response.body[3].length > 0) {
		   	console.log(keyword + ": " + response.body[3][0])
		   	fs.appendFile(fileName + '.log',  keyword + ": " + response.body[3][0] + '\n', function (err) {})
		} else {
			console.log(keyword + ": No Result")
		   	fs.appendFile(fileName + '.log',  keyword + ": No Result" )
		}
	})
}