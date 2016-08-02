import sys
import argparse
import requests
from datetime import datetime

logfile = "result.log"
api_url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search="

def search(keyword):
	logs = open(logfile, "a")
	search_results = requests.get(api_url + keyword)
	results = search_results.json()
	timestmp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	logs.write(timestmp + "  " + results[0] + "  " + results[1][0] + "  " + results[3][0] + "\n")
	return results[3][0]

parser = argparse.ArgumentParser()
parser.add_argument("logfile",nargs = "*", help = "Logs results to this file")
parser.add_argument("query", nargs = "*", help = "Query to be searched for no query starts interactive mode")
args = parser.parse_args()

if len(sys.argv) == 1:
	print "Enter the search term"
	keyword = raw_input()
	print "searching for",keyword
	try:
		result = search(keyword)
	except Exception, ex:
		print ex
		sys.exit()
	print result
else:
	print "searching for",sys.argv[1]
	print search(sys.argv[1])
