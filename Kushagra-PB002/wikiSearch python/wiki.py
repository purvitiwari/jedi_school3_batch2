import argparse
import sys
import requests
from datetime import datetime

api_url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search="

def searchWiki(query, logfile):
	logfile = open(logfile, "a")
	search_results = requests.get(api_url + query)
	results = search_results.json()
	timestmp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	logfile.write(timestmp + "  " + results[0] + "  " + results[1][0] + "  " + results[3][0] + "\n")
	return results[3][0]

parser = argparse.ArgumentParser()
parser.add_argument("logfile", help = "Logs results to this file")
parser.add_argument("query", nargs = "*", help = "Query to be searched for no query starts interactive mode")
args = parser.parse_args()

input_array = sys.argv

if len(input_array) == 2:
	logfile = input_array[1]
	choice = "y"
	while choice =="y" or choice == "Y":
		query = raw_input("Enter the keyword to be searched: ")
		print "Searching...." + query
		try:
			search_link = searchWiki(query, logfile)
		except Exception, e:
			print e
			print "Exiting..."
			sys.exit()
		print "Search Completed"
		print "Link: " + search_link + "\n"
		choice = raw_input("Enter the choice(y/n): ")
else:
	logfile = input_array[1]
	for i in range(2, len(input_array)):
		query = input_array[i]
		print "Searching...." + query
		try:
			search_link = searchWiki(query, logfile)
		except Exception, e:
			print e
			print "Exiting..."
			sys.exit()
		print "Search Completed"
		print "Link: " + search_link + "\n"





