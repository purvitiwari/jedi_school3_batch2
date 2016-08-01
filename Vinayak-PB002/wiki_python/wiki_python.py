import urllib, json,sys

def wikiSearch(searchTerm):
	result = "";
	try:
		url = "https://en.wikipedia.org/w/api.php?action=opensearch&search="+ searchTerm + "&limit=1&format=json";
		response = urllib.urlopen(url);
		data = json.loads(response.read());
		print "Title : " + str(data[1][0]);
		print "URL : " + str(data[3][0]);
		title = str(data[1][0]);
		link = str(data[3][0]);
		result = title + "    " + link;
	except:
		result = "error";
		#print "There was some error!";
	return result;

def writeToFile(result, fileName):
	f = open(fileName, 'a');
	f.write(result + "\n");
	f.close();

searchTerm = "";
fileName = "";
if(len(sys.argv) > 1):
	searchTerm = sys.argv[1];
	fileName = sys.argv[2];
else:
	searchTerm = raw_input("Enter search item : ");
	fileName = raw_input("Enter log file name : ");
searchTerm = searchTerm.replace(' ', '');
result = wikiSearch(searchTerm);
if(result == "error"):
	print "There was some error!!";
else:
	writeToFile(result, fileName);
