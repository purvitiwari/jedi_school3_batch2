console.log("############################################################################");
console.log("################## Please Install 'npm install validator' ##################");
console.log("############################################################################");
console.log("############################################################################");
console.log("################      Only Indian, US, French and Chinese ##################");
console.log("#######################      Numbers are supported.   ######################");
console.log("############################################################################");
console.log("############################  India ----- in          ######################");
console.log("############################  United States-- us      ######################");
console.log("############################  French ---- fr          ######################");
console.log("############################  CHinese ---- cn         ######################");
console.log("############################################################################");
console.log("############################################################################");



var firstDig;
var flag = false;
var readline = require('readline');

function checkIndianPhoneNumber(){
	var rl = readline.createInterface(process.stdin, process.stdout);
	rl.setPrompt('At any time to exit Type lol > ');
	console.log("##################################################################");
	console.log("####################   For Indian Numbers    #####################");
	console.log("##################################################################");
	rl.prompt();
	rl.on('line', function(line) {
	    if (line === "lol")  rl.close();
		var intNum = parseInt(line);
		//Proceeds iff input is number
	    if(!isNaN(intNum)){
	    	var n = line.length;
	    	if(n == 10 || n == 11){
	    		flag = true;
	    		if(n == 10){
	    			firstDig = line.substr(0,1);
	    			if( parseInt(firstDig) <= 9 && parseInt(firstDig) >=7){
	    				console.log("Its Valid 10 digit Indian number!!!.................... Good go on.................");
	    			}
	    			else{
	    				console.log("This 10 digit number does not starts from 7,8 or 9");
	    			}
	    		}
	    		firstDig = line.substr(1,1);
	    		var isZero = line.substr(0,1);
	    		if(n == 11){
	    			if( parseInt(firstDig) <= 9 && parseInt(firstDig) >=7 && parseInt(isZero) == 0){
	    				console.log("Its Valid 10 digit Indian number!!! .......................... Good go on..................");
	    			}
	    			else{
	    				console.log("This 10 digit number does not starts from 7,8 or 9");
	    			}
	    		}
	    	}
	    	else if(flag == false ||  n == 13){
			   	var validator = require('validator');
			 	var isCheck = validator.isMobilePhone(line,'en-IN');
				if(!isCheck){
			 		console.log("ts not Valid Phone number !!!");
			 	}
			 	else console.log("Its Valid 10 digit Indian number!!! ...............................Good go on...............");
		 	}
	    	else
	    		console.log("Its not Valid Phone number");
		}
	    else{
	    	console.log("Input is Not a Valid Number.");
	    }
	    rl.prompt();
	}).on('close',function(){
		console.log("##################################################################");
		console.log("####################   Thank You for Using   #####################");
		console.log("##################################################################\n");
	    process.exit(0);
	});
}
function checkUSPhoneNumber(){
	var rl = readline.createInterface(process.stdin, process.stdout);
	rl.setPrompt('At any time to exit Type lol > ');
	console.log("##################################################################");
	console.log("####################   For US Numbers    #####################");
	console.log("##################################################################");
	rl.prompt();
	rl.on('line', function(line) {
	    if (line === "lol")  rl.close();
		var validator = require('validator');
		var isCheck = validator.isMobilePhone(line,'en-US');
		if(!isCheck){
			console.log("ts not Valid US Phone number !!!");
		}
		else 
			console.log("Its Valid 10 digit US Phone number!!! ..................Good go on..........................");
	    rl.prompt();
	}).on('close',function(){
		console.log("##################################################################");
		console.log("####################   Thank You for Using   #####################");
		console.log("##################################################################\n");
	    process.exit(0);
	});
}
function checkFrenchPhoneNumber(){
	var rl = readline.createInterface(process.stdin, process.stdout);
	rl.setPrompt('At any time to exit Type lol > ');
	console.log("##################################################################");
	console.log("####################   For France Numbers    #####################");
	console.log("##################################################################");
	rl.prompt();
	rl.on('line', function(line) {
	    if (line === "lol")  rl.close();
		var validator = require('validator');
		var isCheck = validator.isMobilePhone(line,'en-fr');
		if(!isCheck){
			console.log("ts not Valid French Phone number !!!");
		}
		else 
			console.log("Its Valid 10 digit French Phone number!!! ..................Good go on..........................");
	    rl.prompt();
	}).on('close',function(){
		console.log("##################################################################");
		console.log("####################   Thank You for Using   #####################");
		console.log("##################################################################\n");
	    process.exit(0);
	});
}
function checkChinesePhoneNumber(){
	var rl = readline.createInterface(process.stdin, process.stdout);
	rl.setPrompt('At any time to exit Type lol > ');
	console.log("##################################################################");
	console.log("####################   For Chinese Numbers    #####################");
	console.log("##################################################################");
	rl.prompt();
	rl.on('line', function(line) {
	    if (line === "lol")  rl.close();
		var validator = require('validator');
		var isCheck = validator.isMobilePhone(line,'zh-CN');
		if(!isCheck){
			console.log("ts not Valid Chinese Phone number !!!");
		}
		else 
			console.log("Its Valid 10 digit Chinese Phone number!!! ..................Good go on..........................");
	    rl.prompt();
	}).on('close',function(){
		console.log("##################################################################");
		console.log("####################   Thank You for Using   #####################");
		console.log("##################################################################\n");
	    process.exit(0);
	});
}
//checkIndianPhoneNumber();
console.log("Please Enter the Country Code as shown above .. ");
var readline = require('readline');
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', function(line){
    //console.log(line);
    if(line == "in") checkIndianPhoneNumber();
    if(line == "us") checkUSPhoneNumber();
    if(line == "fr") checkFrenchPhoneNumber();
    if(line == "cn") checkChinesePhoneNumber();
    else if(line === "exit") rl.close();
}).on('close',function(){
	process.exit(0);
});



// var stdin = process.openStdin();
// stdin.addListener("data", function(d) {
//     // note:  d is an object, and when converted to a string it will
//     // end with a linefeed.  so we (rather crudely) account for that  
//     // with toString() and then trim() 
//     console.log("you entered: [" + 
//         d.toString().trim() + "]");
//   });



// 'ar-SY', 'cs-CZ', 'de-DE', 'da-DK', 'el-GR', 'en-AU', 'en-GB', 'en-HK', 'en-IN', 'en-NZ', 'en-US', 'en-CA', 'en-ZA', 'en-ZM', 'es-ES', 'fi-FI', 'fr-FR', 'hu-HU', 'ms-MY', 'nb-NO', 'nn-NO', 'pl-PL', 'pt-PT', 'ru-RU', 'tr-TR', 'vi-VN', 'zh-CN', 'zh-TW'
// Arabic - Algeria	ar	ar-dz
// Arabic - Syria	ar	ar-sy
// Czech	cs	cs
// German - Germany de-DE
// Danish	da	da




