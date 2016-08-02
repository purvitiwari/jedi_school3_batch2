import urllib
import ast
import sys


def get_details(search_term):
	url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + \
	search_term + "&limit=1&namespace=0&format=json"
	filehandle = urllib.urlopen(url)
	obj = filehandle.read()
	output = ast.literal_eval(obj)
	if not output[1]:
		to_be_written = "\"" + output[0] + "\" : " + \
		"Word not found in Wikipedia"
	else:
		to_be_written = "\"" + output[1][0] + "\" : " + output[3][0]
	print to_be_written
	f = open('log.txt','a')
	f.write(to_be_written)
	f.write("\n")
	f.close()
	return


def interactive_mode():
	print "Enter search term"
	print "NOTE : Enter \"exit\" to exit"
	search_term = raw_input()
	while search_term!="exit":
		output = get_details(search_term)
		print "Enter search term"
		print "NOTE : Enter \"exit\" to exit"
		search_term = raw_input()

	if search_term=="exit":
		raise SystemExit
	return


def get_help():
	print "--help : To display help"
	print "--search <space> search_term : To search word on wikipedia in argument mode"
	print "Enter search_term inside \"\" if search_term more than one word"
	print "-i : To go to interactive mode"
	return


def check_valid_arg():
	if len(sys.argv)==2 and sys.argv[1]=="--help" :
		get_help()
	
	elif len(sys.argv)==3 and sys.argv[1]=="--search" :
		get_details(sys.argv[2])

	elif len(sys.argv)==2 and sys.argv[1]=="-i" :
		interactive_mode()

	else:
		print "Invalid usage"
		get_help()

	return
	raise SystemExit


check_valid_arg()