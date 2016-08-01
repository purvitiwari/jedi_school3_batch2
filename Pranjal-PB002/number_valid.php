<?php
////////////////////////////////////////////////////////////////////////////////
// PHONE NUMBER VALIDATION PHP CLI SCRIPT
// Usage &>php  numberValidator.php [-cli/-int] [optional for -cli -phone phoneNumber]
// -cli for command line interface and -int for interactive mode
// Example &>php numberValidator.php -cli -phone +91-9666837027";
// Example &>php numberValidator.php -int";
// Designed pranjalk
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// Future improvement :  if only ten digits are given then ask for country code??
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
//// FUNCTIONS START HERE!
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// function to check the phone number from numerify api
// WARNING! DO NOT COPY THE API KEY!!!!!!
function validateNumber ($phoneNumber) {
  echo "the entered phone number is $phoneNumber";
  echo "\n";
  $accessKey = "5897967950821a17fbff92b7cc531bb9";
  $apiLocation = "http://apilayer.net/api/validate";
  $apiUrl = $apiLocation . "?access_key=" . $accessKey . "&number=" . $phoneNumber . "&format=1";
  // echo $apiUrl;
  $curl = curl_init($apiUrl);
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
  $curl_response = curl_exec($curl);
  if ($curl_response === false) {
      $info = curl_getinfo($curl);
      curl_close($curl);
      die('\nerror occured during curl exec. Additioanl info: ' . var_export($info));
  }
  curl_close($curl);
  $validationData = json_decode($curl_response);
  $validCheck = $validationData->valid;
  if ($validCheck == true) {
    echo "\n THE PHONE NUMBER IS VALID \n";
    echo "Phone Number : ";
    echo $validationData->number;
    echo "\nLocal Format : ";
    echo $validationData->local_format;
    echo "\nInternatioal Format : ";
    echo $validationData->international_format;
    echo "\nCountry Prefix : ";
    echo $validationData->country_prefix;
    echo "\nCountry Code : ";
    echo $validationData->country_code;
    echo "\nCountry Name : ";
    echo $validationData->country_name;
    echo "\nLocation : ";
    echo $validationData->location;
    echo "\nCarrier : ";
    echo $validationData->carrier;
    echo "\nLine Type : ";
    echo $validationData->line_type;
    echo "\n";
  } else {
    echo "The phone number $phoneNumber is INVALID!";
  }
}
//function to print invalid usage
function invalidUsage() {
  echo "\nINVALID USAGE!";
  echo "\nUsage &>php  numberValidator.php [-cli/-int] [optional for -cli -phone phoneNumber]";
  echo "\nExample &>php numberValidator.php -cli -phone +91-9666837027\n\n";
}

////////////////////////////////////////////////////////////////////////////////
//// FUNCTIONS ENDS HERE!
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
//// MAIN PROGRAM STARTS HERE!
////////////////////////////////////////////////////////////////////////////////
$interactiveflag = 1;
if(strcmp($argv[1],"-cli") == 0) { //if the first argument is -cli
  if($argc != 4) { //check if all the appropiate arguments are given in command line
    invalidUsage();
  } else { // if proper entry into CLI mode
    if(strcmp($argv[2],"-phone") != 0) {
      invalidUsage();
    } else {
      $inputNumber = $argv[3];
      validateNumber($inputNumber);
    }
  }
} elseif (strcmp($argv[1],"-int") == 0) { // if first arguement is -int
  if($argc != 2) { //check if all the appropiate inputs are given in interactive mode
    invalidUsage();
  } else { // if proper entry in INTERACTIVE MODE!
    while ($interactiveflag) {
      $inputNumber = readline("\nEnter the phone number : ");
      validateNumber($inputNumber);
      $checkContinueInteractive = readline("\nDo you want to check another number? <yes/no>");
      if(strcmp($checkContinueInteractive,"yes") == 0){
        $interactiveflag = 1;
      } elseif(strcmp($checkContinueInteractive,"no") == 0) {
        echo "\nThank you for using the number validation script!";
        echo "\n Have a good day!\n\n";
        $interactiveflag = 0;
      } else {
        echo "\n Invalid Input.. quitting!\n\n";
        $interactiveflag = 0;
      }
    }
  }
} else {
  invalidUsage();
}
////////////////////////////////////////////////////////////////////////////////
//// MAIN PROGRAM ENDS HERE!
////////////////////////////////////////////////////////////////////////////////
