import json
import requests
import sys
import os
import argparse

def check_exit(query):
	if query.strip().lower() == "exit":
		exit()
	return False

def get_url(file, query):
	api_url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search="+query
	try:
		response = requests.get(api_url)
	except requests.exceptions.RequestException as e:
		print e
		return
	json_data = response.json()
	url = json_data[3]
	if len(url) > 0:
		file.write(json_data[3][0]+'\n')
		print '-'*50,'\n',json_data[3][0],'\n','-'*50
	else:
		print '-'*50,'\n',"No Search found",'\n','-'*50

def main():
	parser = argparse.ArgumentParser(description = 'Wikepidia search')
	parser.add_argument("-f", "--file",dest = "file", help = "File for logging the urls")
	parser.add_argument("-q", "--query",dest = "query", help = "Search query for Wikipedia",nargs='+')
	arguments = parser.parse_args()

	query = ''
	length_argv = len(sys.argv)
	file_name = ''
	
	if arguments.file:
		file_name = arguments.file
	else:
		file_name = raw_input("Enter the logging file :")
	
	file = open(file_name, "a")
	if arguments.query:
		for i in arguments.query:
			query += i
			get_url(file, query)
	while(1):
		query = raw_input("Enter the Search or enter \"exit\" to quit :")
		if not len(query):
			continue
		check_exit(query)
		get_url(file, query)
		
		

if __name__ == "__main__":
	main()