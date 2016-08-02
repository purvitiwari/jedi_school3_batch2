import requests
import json
import logging
from requests.exceptions import ConnectionError
import sys
import datetime


def queryfunction(query, file):

    api_url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search="+query

    try:
        myResponse = requests.get(api_url)
        if(myResponse.ok):
            final_key=""
            jData = json.loads(myResponse.content)
            for key in jData:
                final_key=json.dumps(key)
        url = final_key[2:-2]
        logging.basicConfig(filename=file,level=logging.DEBUG)
        logging.info(str(datetime.datetime.now())+ "   " +url)
        print url

    except ConnectionError as e:
        r = "Error Connecting"
        print r

    

#if command line arguments are present 2nd is query with no space 1st is filename    
try:
    
    filename=sys.argv[1]
    query=sys.argv[2]
    for i in range(3,len(sys.argv)):
        query=query+" "+sys.argv[i];
    queryfunction(query,filename)
    
except:
    query = raw_input("Please enter your search query for wikipedia : ")
    file= raw_input("Please enter the filename : ")
    file=file+".log"
    queryfunction(query,file)
    
