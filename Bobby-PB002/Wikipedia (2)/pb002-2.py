import sys
import requests
import json 
def searcher(tosearch,tosotore):
	try:
 		wikistr=requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&search="+tosearch+"&limit=1&format=json")
		if(wikistr.status_code==200):
			content=wikistr.content
			o = json.loads(content)
			print "The title of your page is "+o[1][0]
			print "The link of your page is "+o[3][0]
			tosotore.write(tosearch+" rendered "+o[3][0])
			tosotore.write("\n")
		else:
			print "There seems to be an issue in contacting the server"
	except requests.ConnectionError, e:
		print "There seems to be an issue in connecting to the server"
	return(0);
if len(sys.argv)>=2:
	if len(sys.argv)>=3:
		tosotore=sys.argv[1]
	else:
		tosearch=raw_input("Please Enter the string that you want to search : ")
	tosotore=sys.argv[1]
else:
	tosotore=raw_input("Please enter the name of the log file:")
	tosearch=raw_input("Please Enter the string that you want to search : ")
try:
	f=open(tosotore,"w")
except Exception, e:
	"It seems we cant access your file"
	exit()
searcher(tosearch,f)
cont=raw_input("Press one of the following:\n1 to search again\n2 to exit\n:")
while(cont!='2'):
	tosearch=raw_input("Please Enter the string that you want to search : ")
	searcher(tosearch,f)
	cont=raw_input("Press one of the following:\n1 to search again\n2 to exit\n:")	
	exit()
