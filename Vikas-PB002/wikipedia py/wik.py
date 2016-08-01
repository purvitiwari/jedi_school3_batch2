import wikipedia
import time
import datetime

logfile = open("wik.log", "a")
flag = 'true'
while flag == "true" :
	name=raw_input("enter name.\n")

	rest = wikipedia.search(name, results=2, suggestion = False)
	ny = wikipedia.page(rest)
	url = ny.url

	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	logfile.write(st+ " + Name= "+name+" Link = "+url+  "\n \n")

	term = raw_input("Do You want to continue searching y or n.\n ")
	if term == 'y':
		flag = "true"
	elif term == 'n':
		flag = "false"
	else:
		print "invalid input"
		flag = "false"

