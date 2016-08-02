import argparse
import phonenumbers
import sys
parser = argparse.ArgumentParser(description='Check if a phone number is valid or not on the basis of country code if country code is not correct it might give incorrect result')

parser.add_argument(
  '--phonenumber',
  type=str,
  help="Number to be validated"
)

parser.add_argument(
  '--countrycode',
  type=str,
  help="Two digit country code.Eg. INDIA - IN"
)
args = parser.parse_args()

def check_valid(phone,code):
	try:
		if phonenumbers.is_valid_number(phonenumbers.parse(phone, code)):
			print "Valid Number"
		else :
			print "Invalid Number"
	except phonenumbers.phonenumberutil.NumberParseException, e:
		print "Invalid Number"


phoneNumber = ""
countryCode = ""

if args.phonenumber != "":
	phoneNumber = args.phonenumber
if args.countrycode != "":
	countryCode = args.countrycode
	

if not phoneNumber:
	print ("Since phone number was not passed in argument starting interactive mode")
	phoneNumber = raw_input("Enter number u wish to check --- ")
	if "+" not in phoneNumber :
		countryCode = raw_input("Country code 2 character.eg IN for India --- ")
	else:
		countryCode = ""
	check_valid(phoneNumber,countryCode)

else :
	print phoneNumber
	print countryCode
	if countryCode=="":
		if "+" not in phoneNumber:
			print "Country code missing.Either give it with phone number or pass it separately"
			print "Example for India pass IN or +91 in number"
	else:
		check_valid(phoneNumber,countryCode);
