<?php
error_reporting(E_ALL ^ E_WARNING); 
if (count($argv) == 1) {
	echo "Enter a query : ";
	$topic = fgets(STDIN);
	echo "Enter a file name : ";
	$fileName = fgets(STDIN);
	queryfunction($topic, $fileName);
} else { 
	$fileName=$argv[1];
	$topic=$argv[2];
	for ($i=3;$i<count($argv);$i++){
		$topic=$topic."%20".$argv[$i];
	}
	queryfunction($topic, $fileName);
}


function queryfunction($topic, $fileName){
	$topic= str_replace(' ', '%20', $topic); 
	$url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=".$topic;
	
	try {
		$json = file_get_contents($url);
		$json_data = json_decode($json, true);
		foreach ($json_data as $k=>$v){
		}
		$final_url= $v[0]; 
		$date= date('Y-m-d H:i:s');
		file_put_contents($fileName, print_r($final_url." ".$date."\n", true), FILE_APPEND);
		echo($final_url);
	} 
	catch (Exception $e) {
    	echo 'Error: ',  $e->getMessage(), "\n";
	}
	
}

?>