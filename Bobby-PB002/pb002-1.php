<?php
$f = fopen( 'php://stdin', 'r' );
if($argv[1])
{
	$tomatch=$argv[1];
}
else
{
	echo "\nPlease enter the number that you want to validate\n";
	$tomatch=fgets($f);
}
if(preg_match("/^{[0]|[+91]}?[789]\d{9}$/", $tomatch)) {
echo "\n your number is valid\n";
}
else
{
	echo "\n Your number is not valid\n";
}

?>