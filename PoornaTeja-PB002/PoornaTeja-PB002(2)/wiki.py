#####            Documentation          #####

#####    It fetches the wikipedia link for search stream and append to the log file    #####

#####    Code takes commandline arguments  wiki.py [log filename] [search stream]   ######

#####    It aslo asks prameters later if they are not provide in the Interactive mode #####
 



import sys
import requests
import json


def main():
	commandline_arguments = len(sys.argv)
	log_file = ''
	search_string = ''
	if commandline_arguments > 1 :
		log_file = open(sys.argv[1],'a')
	else:
		log = raw_input('Enter log filename : ')
		log_file = open(log,'a')
	if commandline_arguments > 2 :
		search_string = sys.argv[2]
	else:
		search_string = raw_input("Enter the Search String: ")
	data = api_request(search_string)
	if len(data[-1]) > 0:
		log_file.write(data[-1][0]+ '\n')
	else:
		log_file.write('No Link Exists\n')
	log_file.close()

def api_request(search_string):
	url = 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + search_string + '&limit=1&namespace=0&format=json'
	try:
		response = requests.request('GET',url)
		data = json.loads(response.text)
		return data
	except requests.exceptions.RequestException as e:
		print e
		return [[str(e)]]


if __name__ == "__main__" :
	main()