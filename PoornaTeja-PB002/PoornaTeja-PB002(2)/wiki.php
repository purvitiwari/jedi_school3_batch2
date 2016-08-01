
<?php

//            Documentation          

//    It fetches the wikipedia link for search stream and append to the log file    

//    Code takes commandline arguments  wiki.py [log filename] [search stream]   

//    It aslo asks prameters later if they are not provide in the Interactive mode 

$numargs = sizeof($argv);
if($numargs > 2)  	
{
	$logfile_name = $argv[1];
	for($i=2;$i<$numargs;$i++)
		$query=$query.$argv[$i];
}
elseif ($numargs > 1) {
	$logfile_name = $argv[1];
	echo "Enter the Search Stream : ";
	$temp = fopen("php://stdin", "r");
	$query = fgets($temp);
}
else
{
	echo "Enter the name of logfile : ";
	$temp = fopen("php://stdin","r");
	$logfile_name = fgets($temp);
	echo "Enter the Search Stream : ";
	$temp1 = fopen("php://stdin", "r");
	$query = fgets($temp1);
}
try {
	$response = file_get_contents("https://en.wikipedia.org/w/api.php?action=opensearch&search=".$query."&limit=1&namespace=0&format=json",false);
	$data = json_decode($response, true);
	$logfile= fopen($logfile_name,"a");
	try {
		fwrite($logfile, $data[3][0]."\n");
		fclose($logfile); 	
	 } catch (Exception $e) {
	 	$err = "No Article Avaliable";
	 	fwrite($logfile, $err."\n");
	 	fclose($logfile);
	 } 
} catch (Exception $e) {
    #echo 'Caught exception: ',  $e->getMessage(), "\n";
    $err = $e;
    fwrite($logfile, $err."\n");
	fclose($logfile);
}

?>