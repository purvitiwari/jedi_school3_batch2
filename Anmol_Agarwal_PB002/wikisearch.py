import sys
import datetime
import requests
import json
import logging
from requests.exceptions import ConnectionError

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        logFile = sys.argv[1]
        search_term = ""
        argvLength = len(sys.argv)
        for i in range(3, argvLength):
            search_term += sys.argv[i]
    else:
        logFile = raw_input("Enter the log file name\n")
        search_term = raw_input("Enter the search term\n")

    searchUrl = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=" + search_term

    try:
	logging.basicConfig(filename = logFile, level = logging.DEBUG)
        response = requests.get(searchUrl)
        if response.ok:
            str_data = ""
            data_in_json = json.loads(response.content)
            for url in data_in_json:
                str_data = json.dumps(url)
        link = str_data[2:-2]
        logging.info(str(datetime.datetime.now())+ "   " + link)


    except ConnectionError as event:
        print "Internet Connection seeems not working"

    
