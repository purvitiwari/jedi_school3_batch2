#!/usr/bin/env node
'use strict'

var program = require('commander');
var request = require('request');

let validate_number = (number,option) => {
	var url = "http://apilayer.net/api/validate?access_key=9219e606b830fb22c5b055ee2a545e4a&number=" + number + "&country_code=&format=1";
	request(url, function(error, response, body) {
		if(!error && response.statusCode==200) {
			var obj = JSON.parse(body);
			if(obj["valid"]==true) {
				console.log(number + " is valid");
				console.log("country : " + obj["country_name"]);
			}
			else {
				console.log(number + " is invalid");
			}
		}
	})
}

program
	.version('1.0')
	.command('[number]','Number to be validated')
	.description('CLI for validation of phone numbers')
	.action(validate_number);
program.parse(process.argv);

