<?php

if(sizeof($argv) > 1) {
	$query = $argv[1];
}
else {
	echo "Enter the search term\n";
    $stream = fopen("php://stdin", "r");
    $query = fgets($stream);
}

$filename = fopen("linksLogs.log", "a");

try {
    $response = file_get_contents("https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=".$query, false);
    $result = json_decode($response, true);
    fwrite($filename, $result[3][0]."\n");
    fclose($filename);
} catch (Exception $e) {
    fwrite($filename, $e, "\n");
    fclose($filename);
}

?>