import argparse
import json
import sys
import requests


parser = argparse.ArgumentParser(description='Search result for top title in wiki search bar'+'\n'+
	'give log file name as argument else it will save it to log.txt')

parser.add_argument(
  '--filename',
  type=str,
  help="logfile name in which result will be appended"
)

flag = 1;

parser.add_argument(
  '--keyword',
  type=str,
  help="word to be searched"
)
args = parser.parse_args()
file = ""
keyword = ""

if args.filename != "":
	file = args.filename
if args.keyword != "":
	keyword = args.keyword

if file is None:
	print "Will write to log.txt"
	file = 'log.txt'
else:
	file = str(file)+'.txt'

if keyword is None:
	print ("Entered intractive mode")
	flag = 0
	keyword = raw_input("Enter word to be searched -- ")

f1=open(file,'a')
#res = requests.get('https://en.m.wikipedia.org/w/api.php?action=query&format=json&prop=pageprops%7Cpageprops%7Cpageimages%7Cpageterms&generator=prefixsearch&ppprop=displaytitle&pithumbsize=80&pilimit=15&wbptterms=description&gpssearch='+keyword+'&gpsnamespace=0&gpslimit=15')
res = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&search='+keyword)
if flag == 0:
	print "fetching all results ..........."
	jsonResults = json.loads(str(res.text))
	print "titles of top result"
	i = 0;
	if len(jsonResults)>2:
		for x in jsonResults[1]:
			print x
		f1.write(jsonResults[3][0])
		f1.write('\n')
		print jsonResults[3][0]
	else :
		print "No result"
else :
	jsonResults = json.loads(str(res.text))
	if len(jsonResults)>2:
		f1.write(jsonResults[3][0])
		f1.write('\n')
	else :
		print "No result"


