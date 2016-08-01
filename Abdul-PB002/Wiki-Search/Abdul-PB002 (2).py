import requests
import sys
import json
import argparse
from datetime import datetime as dt

EXCEPTION_NONE = 0
EXCEPTION_VALUE_ERROR = 1

# Queries the API for a word and return the
# data and handles exception if something goes wrong
def getSearchResult(API_URL, query):
	payload = dict(
				action = 'opensearch',
				search = query,
				limit = '1',
				format = 'json'
				)
	try:
		result = requests.get(API_URL, params=payload)
		result = result.json()
		return EXCEPTION_NONE, result
	except ValueError as e:
		print "API returned no content\n"
		return EXCEPTION_VALUE_ERROR, None
	except requests.exceptions.RequestException as e:
		print "Something Went Wrong. Error Details"
		print e
		print "Exiting the program.\n"
		sys.exit(1)

# opens a file and returns a handler to it
def getLogFile(filename):
	logFile = None
	try:
		logFile = open(filename,'a')
	except IOError as e:
		print "Unable to open File\n"
		print e
		print "Cannot proceed. Terminating........."
		return None
	return logFile

# parse and save the data to the file
def saveLogtoFile(logFile, query, data, currentTime):
	try:
		title = data[1][0]
		url = data[3][0]
		dumpData = "{'Query': "+str(query)+", Time : "+ \
		currentTime+", 'Title' : "+str(title)+", 'URL' : "+str(url)+"})"+"\n"
		logFile.write(dumpData)
		print "Data saved in LogFile\n"
	except IOError as e:
		print "Unable to write to File\n"
		print e
	
	except ValueError as e:
		# print eof
		# print "Value Error"
		print "Wikipedia returned nothing\n"
	
	except IndexError as e:
		# print "Index Error"
		print "Wikipedia returned nothing\n"


def main():
	API_URL = "https://en.wikipedia.org/w/api.php"
	query = ""
	current_time = ""
	# Parser for the command line inputs # 
	parser = argparse.ArgumentParser(description=
		'Query a word to wikipedia and logs the links in a file')
	parser.add_argument('Filename', metavar='Filename', nargs=1,
						help='Log file')
	parser.add_argument('SearchQuery', metavar="QueryString", nargs='?',
						help='Search query string for wikipedia')
	args = parser.parse_args()
	####################################
	
	######### Opening Log File #########
	logFile = getLogFile(args.Filename[0])
	if not logFile:
		sys.exit(1)
	#########################################

	# Query Processing ######################
	

	if args.SearchQuery != None:	#If query is passed with command line
		print "You have passed "+args.SearchQuery + " as the search query\n"
		query = args.SearchQuery
	else:							#If query is not passed with command line	
		query = raw_input("Enter a search query string: ")
	
	#Runs untill user wants it to run
	while  query != "e" and query != "q" : 
		
		print "Fetching Data from Wikipedia..."
		current_time = str(dt.now()) # Recording the time of search
		returnCode, data = getSearchResult(API_URL,query)
		print "Done\n"


		if returnCode == EXCEPTION_NONE:	#If there is no error in API call
			saveLogtoFile(logFile, query, data,current_time)
		
		#Asks for another query or exit
		query = raw_input("Enter another query or type q or e to exit: ")

	# Gracefully closes the file
	try:
		logFile.close()
	except IOError as e:
		print e


if __name__ == '__main__':
	main()
