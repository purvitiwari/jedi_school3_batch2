import urllib
import requests
import argparse

def log(url, logFile):
  with open(logFile, "a") as out:
    out.write(url + "\n")

def searchWiki(term, logFile):
  print "Searching Wikipedia for \"" + term + "\" ...\n"
  term = urllib.quote_plus(term)
  apiUrl = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=" + term
  try:
    response = requests.get(apiUrl)
  except requests.exceptions.RequestException as e:
    print e
    exit(1)
  
  requestData = response.json()
  url = requestData[3][0]
  print requestData[1][0], "\n\n", requestData[2][0], "\n\n", url
  
  log(url, logFile);

logFileName = ""
searchTerm = ""

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log-file", help="Name of the log file")
parser.add_argument("-q", "--query", help="Query string")
args = parser.parse_args()

if (args.log_file):
  logFileName = args.log_file
else:
  logFileName = raw_input("Enter log file name: ")

if (args.query):
  searchTerm = args.query
else:
  searchTerm = raw_input("Enter search term: ")
  
searchWiki(searchTerm, logFileName)