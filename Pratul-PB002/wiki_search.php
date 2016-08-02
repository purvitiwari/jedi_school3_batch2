<?php

if(sizeof($argv) == 1) {
	echo "Enter the keyword\n";
	$stream = fopen("php://stdin", "r");
	$query = fgets($stream);
}
else {
	$query = $argv[1];
	echo "Search term\n";
	echo $query."\n";
}

$logfile_name = "results";
$logfile = fopen("results.log", "a");

try {
	$response = file_get_contents("https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=".$query,false);
	$result = json_decode($response, true);
	fwrite($logfile, $result[3][0]."\n");
	fclose($logfile);
	echo $result[3][0]."\n";
} catch (Exception $e) {
	fwrite($logfile, $e, "\n");
	fclose($logfile);
}

?>