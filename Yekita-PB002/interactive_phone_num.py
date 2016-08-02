import sys
import urllib2
import json

l = len(sys.argv)
number = None
country_code = None
if l == 2:
	country_code = "IN"
	number = sys.argv[1]
elif l == 3:
	country_code = sys.argv[1]
	number = sys.argv[2]
elif l == 4:
	country_code = sys.argv[2]
	number = sys.argv[3]

def search_phone_num(number):
	url = "http://apilayer.net/api/validate?access_key="
	access_key = "6a0807ac20a19e16aeb14d39e9d8ad18"
	request = url + access_key + "&number=" + number + "&country_code=" + country_code + "&format = 1"
	content = urllib2.urlopen(request).read()
	data = json.loads(content)
	if data["valid"]:
		print 'Given number is valid'
		print 'line type : ', data["line_type"]
		print 'country_name', data["country_name"]
		print 'location : ', data["location"]
	else:
		print 'Given number is invalid'

if l == 4 and sys.argv[1] == '-i':
	search_phone_num(number)
	while(1):
		ans = raw_input('You want to continue to search more (y/n)')
		if ans == 'y' or ans == 'yes':
			number = raw_input("Enter the Number : ")
			search_phone_num(number)
		else:
			break
else:
	search_phone_num(number)

