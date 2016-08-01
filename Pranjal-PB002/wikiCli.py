import urllib2
import json
import sys
import time
import datetime

def logWrite(input_string):
    if(len(sys.argv) == 4):
        if(sys.argv[3] == "-l"):
            log_file = open("wikiCli.log", "a")
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            log_string = (timestamp + " : " + input_string)
            log_file.write(log_string + "\n")
            log_file.close()

def printHelp():
    print "Usage: python wikiCli.py [OPTIONS] [LOG enable/disable]\n"
    print "OPTIONS:"
    print "--help, -h : Display the help section"
    print "--search <string>, -s <string> : search string for wikipedia"
    print "--log, -l: enable or disable log to a file "
    print "NOTE: the log entry will be appended to the same file"
    print "if the file does not exist will be created"
    print "Example : python wikiCli.py -[sh] <string> -l\n"

def search(search_string):
    apiResult =  urllib2.urlopen("https://en.wikipedia.org/w/api.php?action=opensearch&search=" + search_string + "&limit=1&namespace=0&format=json").read()
    apiResult = str(apiResult)
    apiResult = apiResult.split(",")
    JSONparse = apiResult[len(apiResult)-1]
    JSONparse = JSONparse.replace("[","")
    JSONparse = JSONparse.replace("]","")
    JSONparse = JSONparse.replace("\"","")
    JSONparse = str(JSONparse)
    if JSONparse != "":
        print ("\n" + JSONparse + '\n')
        logWrite(JSONparse)
    else:
        print( search_string + " does not exist in wikipedia!")
        logWrite( " does not exist in wikipedia!")

if(len(sys.argv) < 2):
    print "\nInvalid Usage \n"
    printHelp()
    exit()
if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
    if(len(sys.argv) != 2):
        print "Invalid Usage \n"
        printHelp()
        exit()
    else:
        printHelp()
        exit()
elif(sys.argv[1] =="--search" or sys.argv[1] == "-s"):
    if(len(sys.argv) > 5 and len(sys.argv) < 2):
        print ("Invlid Usage")
        printHelp()
        exit()
    else:
        search(sys.argv[2])
