################
##
#
#  PB002 CLI COMMANDS
#  Instructor  Mr. Tushar Babbar
#  Submitted By: Riya Garg
#  Emp id. P2958
#
#
# In the augment mode:
# the command line input must be given in inverted commas 
#
# for e.g. python wiki.py  file_name.txt "sachin tendulkar" 
#
# term=sachin tendulkar file_name=logs
# the output which will append in the log file is:
# 208.80.154.224 [2016-07-28 18:42:24] sachin tendulkar https://en.wikipedia.org/wiki/Sachin_tendulkar
#
#
#################

import re
import sys
import urllib2,socket,urlparse
import json
import datetime
import argparse


# @description 
# this menthod return the logs which contain the host address , timestamp , title and the article link for the particular search term using the wikipedia API and append the logs into a output file.
#
# * @param mfile {string} : name of the file in which you wanna store logs
# * @param term {string}  : term you wanna search.
# * @return {null} : append the string in the log file

def searchforterm(mfile,term): 
	file = open(mfile, "a")
	
	title=urllib2.quote(term,':/')
	url='https://en.wikipedia.org/w/api.php?action=query&titles='+title+'&prop=info&inprop=url&format=json'

	response = urllib2.urlopen(url)
	string=response.read()

	inf=response.info()
	addr = socket.gethostbyname(urlparse.urlparse(response.geturl()).hostname)

	d = json.loads(string)
	

	for key, value in d['query']['pages'].iteritems():


		time= "["+'{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())+"]"
		link= value['fullurl']
  
	    
		file.write(addr+" "+time +" "+term+" "+ link +"\n")


parser = argparse.ArgumentParser()
parser.add_argument("logfile",nargs = "*", help = "Logs results to this file")
parser.add_argument("query", nargs = "*", help = "Query to be searched for no query starts interactive mode")
args = parser.parse_args()


if(len(sys.argv) ==	1):

 
	print "Welcome to wikipedia page of my MacBook Pro  \n \n  lets start !!! "
	mfile=raw_input("enter the log file name: ")


	ch='y';

	while (ch =="y" or ch=="Y"):
		print "enter the term you wanna search : " 
		term=raw_input()
		searchforterm(mfile,term)
		print"do you wanna search for another term y/n"
		ch=raw_input()
	
	print  "EXIT"

else:
	
	searchforterm(sys.argv[1],sys.argv[2])

	  









