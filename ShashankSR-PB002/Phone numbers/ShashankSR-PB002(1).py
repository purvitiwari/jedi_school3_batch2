import phonenumbers
import argparse,sys

def main(argv):
	#usage = 'usage: \n %prog [options] arg1 arg2 press -h for help.'
	parser = argparse.ArgumentParser(description='Phone number validator using Google phone')
	parser.add_argument("-f", "--file", dest="inputFile",help="file for phone numbers")
	parser.add_argument("-p", "--phone",dest="phone",help="Phone number to validate.")
	parser.add_argument("-c", "--country",dest = "country",help=" Country code to validate.")
	
	opts = parser.parse_args()
	country = None				#TO prevent reference errors.

	if opts.inputFile :
		inputFile = opts.inputFile
	elif opts.phone != None and opts.country != None :
		phone = opts.phone
		country = opts.country 
	else :
		country =  raw_input("Please enter country to validate against :")
		phone =  raw_input("Please enter the Phone number : ")
		
	try:
		x = phonenumbers.parse(phone,country)
		if country:
			if  phonenumbers.is_valid_number(x) :
				print "Valid combinition of number and country"
			else : 
				print "Invalid combinition"
		else :
			print x
	except Exception, e:
		print "Invalid phone number or country code Please use -h for usage"

	

if __name__ == "__main__" :
	main(sys.argv[1:])