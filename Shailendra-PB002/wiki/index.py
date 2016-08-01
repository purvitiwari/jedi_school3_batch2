import requests
import json
import time
import sys
from time import gmtime, strftime

strt = raw_input('Enter the keyword to search: ')

parms = { 'action':'wbsearchentities',
		   'search':strt,
		   'language':'en',
		   'limit':'20',
		   'format':'json'
		 }

print "Requesting the Wekipedia Servers. Hold On...................."

# Requests for Wekipedia api with paramenters defined above
res = requests.get('https://www.wikidata.org/w/api.php',params=parms)

#Results are retrived and converted into dictionary
jsonResults = json.loads(str(res.text))

#If there is valid query
if 'search' in jsonResults:
	#If atleast one results is found
	if jsonResults['search']:
		with open("log.txt", "a") as myfile:
			strToWrite = jsonResults["search"][0]["url"]
			tstamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
			myfile.write(strToWrite+"	"+tstamp+"\n")
			print "Url has been added in the log file."
			myfile.close()
	else:
		print "\nNo matching items are found on server"
else:
	print "\nNo matching items are found on server"


