<?php
function get_url($file,$query)
{
	$api_url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=".$query;
	try {
    	$response = file_get_contents($api_url,false);
	}
	catch (Exception $e) {
		echo $e.'\n';
		return false;
	}
	$json_data = json_decode($response, true);
	$url = $json_data[3];
	if(sizeof($url) > 0){
		echo $url[0].PHP_EOL;
		fwrite($file, $url[0]."\n");
	}
    else{
        echo "No url Found\n";
    }
}

function check_exit($query){
	if(strcmp(strtolower($query),"exit") == 0)
	{
		exit();
	}
	return false;
}
$numargs = sizeof($argv);
if ($numargs == 1){
	echo "Enter the file into which u want to log : ";
	$temp = fopen("php://stdin","r");
	$logfile = fgets($temp);
}
else{
	$logfile = $argv[1];
}
$logfile= fopen($argv[1],"a");
if($numargs>2)  			
{
	for($i=2;$i<$numargs;$i++)
		$query=$query.$argv[$i];
	get_url($logfile, $query);

}
while(1){
	$query = '';
	echo "Enter the search Query or enter \"exit\" to quit : ";
	$temp = fopen("php://stdin","r");
	$query = fgets($temp);
	check_exit($query);
	get_url($logfile, $query);
}
?>