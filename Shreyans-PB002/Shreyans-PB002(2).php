<?php
/*
Wikipedia Search- returns the article related to the query you enter.
add -i for interactive mode
or give query as argument
*/


//gets wiki link from wikipedia api, logs it and returns
function getLink($query) {
	try {
		$wikiLink = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=";
		$data = file_get_contents($wikiLink . $query);
		$link = json_decode($data)[3];
		if (sizeof($link) > 0) {
			try {
				$file = fopen("wiki.php.log", "a");
			}
			catch (Exception $error) {
				$file = fopen("wiki.php.log", 'w');
			}
			fwrite($file, $link[0] . "\n");
			return $link[0];
		}
		else {
			return NULL;
		}
	}
	catch(Exception $error) {
  		echo 'Message: ' .$error->getMessage();
	}
}

// checks for command line arguments
if (sizeof($argv) < 2) {
	echo "Enter Search Query\n";

}

else if (sizeof($argv) == 2 && $argv[1] == '-i') {
	echo "Enter Query or q/Q to Exit: ";
	$handle = fopen ("php://stdin","r");
	$query = fgets($handle);
	while ($query != "q\n" && $query != "Q\n") {
		$link = getLink($query);
		if ($link != NULL)
			echo "Wiki link to your query is: " . $link . "\n";
		else
			echo "Query not Found\n";
		echo "Enter Query or q/Q to Exit:";
		$query = fgets($handle);
	}
}
else {
	$query ="";
	for($i=1;$i<sizeof($argv);$i++) {
		$query = $query.$argv[$i];
	}
	$link = getLink($query);
	if ($link != NULL)
		echo $link."\n";
	else
		echo "Query not Found\n";
}
?>