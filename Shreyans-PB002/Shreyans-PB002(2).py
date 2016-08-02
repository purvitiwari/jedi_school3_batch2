"""
Wikipedia Search- returns the article related to the query you enter.
add -i for interactive mode
or give query as argument
"""

import requests
import sys

wikiLink = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search="

#gets wiki link from wikipedia api, logs it and returns 
def getLink(query):
	try:
		data = requests.get(wikiLink+query)
		if len(data.json()[3]) >0:
			with open("wiki.log", "a") as log:
				log.write(data.json()[3][0]+"\n")
			return data.json()[3][0]
		else:
			return None
	except ValueError:
		print "Unable to connect to wikipedia.org"
		sys.exit(1)

def main():
	if len(sys.argv) < 2:
		print "Enter search query"
		sys.exit(1)
	elif len(sys.argv) == 2 and sys.argv[1] == '-i':
		print "Enter Query or q/Q to Exit:"
		query = raw_input().strip()
		while (query != "q" and query != "Q"):
			link = getLink(query)
			if link != None:
				print "Wiki link to your query is: "+link
			else:
				print "Query not Found"
			print "Enter Query or q/Q to Exit:"
			query = raw_input().strip()
	else:
		query = ' '.join(sys.argv[1:])
		link = getLink(query)
		if link != None:
			print link
		else:
			print "Query not Found"




if __name__ == "__main__":
	main()