import requests
import argparse,sys
from termcolor import colored

def main(argv):
	#usage = 'usage: \n %prog [options] arg1 arg2 press -h for help.'
	parser = argparse.ArgumentParser(description='CLI to save Wiki Search article links. Stores into logfile')
	parser.add_argument("-s", "--search",dest = "search",help="Search phrase")
	parser.add_argument("-f", "--logfile",dest = "logfile",default = "wiki.log",help="Log file to save links")
	opts = parser.parse_args()

	print "INFO : use "+colored("CMD + doubleClick","blue")+"  to view links in browser in mac. -h for help"

	if opts.logfile :
		logfile = opts.logfile
	else :
		print "Saving article links in default log file"

	if not opts.search :
		search = raw_input("Enter search term : ")

	f = open(logfile,'a')
	while search :
		try:
			url = 'https://en.wikipedia.org/w/api.php?format=json&action=opensearch&search='+search+'&limit=1'
			r= requests.get(url)
			print colored(str(r.json()[3][0]),'blue') 				#tech debt. Hardcoded.
			f.write('Searchtext : '+ search + '  URL : ' + str(r.json()[3][0]) +'\n')
			search = raw_input("Enter new search item. (Leave blank to exit) : ")
		except Exception, e:
			print colored("Error Query not found","red")
			search = raw_input("Enter new search item. (Leave blank to exit) : ")
	f.close()	
	print "Search links saved to : " + colored(logfile,"green") + "\n"


if __name__ == "__main__" :
	main(sys.argv[1:])