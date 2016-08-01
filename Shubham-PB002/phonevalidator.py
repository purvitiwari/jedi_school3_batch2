import sys, re

def isValid(phone):
  if(re.match(r'^([0]|[+][9][1])?[7-9]{1}\d{9}$', phone)):
    return True
  else:
    return False

def showVerboseOutput(valid):
  if(valid):
    print "The phone number is valid."
  else:
    print "The phone number is invalid."

argc = len(sys.argv)

if(argc == 2):
  showVerboseOutput(isValid(sys.argv[1]))
elif(argc == 1):
  phone = raw_input("Enter your phone number: ")
  showVerboseOutput(isValid(phone))
else:
  print "Usage:\nisphonevalid [phone number]"