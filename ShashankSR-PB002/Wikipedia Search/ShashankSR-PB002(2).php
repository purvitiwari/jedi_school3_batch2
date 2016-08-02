<?php

//---------------------------------// 

$options = getopt("hf:s:");
if ($options['h'] === false) {
	echo "Usage : CLI = php program [-ffilename] [-ssearch] [-h]\n";
} else {
	if ($options['f']) {
		$filename = $options['f'];
	} else {
		echo "No log file name mentioned. Taking default. See -h for help\n";
		$filename = "wiki.log";
	}
	if ($options['s']) {
		$search = $options['s'];
	}else{
		echo "Please enter a search term.(Leave blank to quit)\n";
		$search = trim(fgets(STDIN));
	}
	$myfile = fopen($filename, "a");
}

//------------------------------------//


while ($search) {
	$query = "https://en.wikipedia.org/w/api.php?format=json&action=opensearch&search=".$search."&limit=1";
	try {
		$response = file_get_contents($query);
		$data = json_decode($response);
		echo "".$data[3][0]."\n";
		fwrite($myfile, $data[3][0]."\n");
	} catch (Exception $e) {
		echo "Error. Query not found";
	}
	echo "Please enter a search term.(Leave blank to quit)\n";
	$search = trim(fgets(STDIN));
	if(!$search){
		fclose($myfile);
		echo "Links saved to ".$filename."\n";
	}
}

?>