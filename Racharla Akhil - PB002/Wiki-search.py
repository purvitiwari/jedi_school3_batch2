import argparse
import json
import requests

def main():
	parser = argparse.ArgumentParser(description='Search result for top title in wiki search bar')

	parser.add_argument('-f', '--fileName', type=str, help='logfile name in which result will be saved')
	parser.add_argument('-k', '--keyword', type=str, help='keyword to be searched')
	args = parser.parse_args()

	#search keyword
	keyword = ''
	if args.keyword != '':
		keyword = args.keyword
		
	if keyword is None:
		keyword = raw_input('Enter keyword to search: ')

	#fileName name
	fileName = ''
	if args.fileName != '':
		fileName = args.fileName

	if fileName is None:
		fileName = raw_input('Enter name of log file: ')

	file = open(fileName + '.log','a')
	res = requests.get('https://en.wikipedia.org/w/api.php?action=opensearch&search=' + keyword)
	jsonResults = json.loads(str(res.text))
	if len(jsonResults) >= 4 and len(jsonResults[3]) >= 1:
		print keyword + ': ' + jsonResults[3][0]
		file.write(keyword + ': ' + jsonResults[3][0])
		file.write('\n')
	else :
		print keyword + ': No Result'
		file.write(keyword + ': No Result')
		file.write('\n')

if __name__ == '__main__':
	main()