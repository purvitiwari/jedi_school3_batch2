
################
## in ruby the wikipedia search 
#
#  PB002 CLI COMMANDS
#  Instructor  Mr. Tushar Babbar
#  Submitted By: Riya Garg
#  Emp id. P2958
#
# In the augment mode:
# the command line input must be given in inverted commas 
# for e.g. python wiki.py  file_name.txt "sachin tendulkar"
#
# term=sachin tendulkar file_name=logs
# the output which will append in the log file is:
# 208.80.154.224 [2016-07-28 18:42:24] sachin tendulkar https://en.wikipedia.org/wiki/Sachin_tendulkar
#
#
##
#################

require 'cgi'
require 'open-uri'
require 'net/http'
require 'json'
require 'socket'

# @description 
# this menthod return the logs which contain the host address , timestamp , title and the article link for the particular search term using the wikipedia API and append the logs into a output file.
#
# * @param mfile {string} : name of the file in which you wanna store logs
# * @param term {string}  : term you wanna search.
# * @return {null} : append the string in the log file

def searchwiki(mfile,term)
	#puts mfile, term
	file= open(mfile, 'a') { |f|

	title=CGI.escape(term)
	#puts title
	url='https://en.wikipedia.org/w/api.php?action=query&titles='+title+'&prop=info&inprop=url&format=json'   
	
	response = Net::HTTP.get_response(URI.parse(url))

	time=Time.now
	time=time.strftime("%Y-%m-%d %H:%M:%S")
	result = JSON.parse(response.body)
    host=UDPSocket.open {|s| s.connect("64.233.187.99",1); s.addr.last}
	
	for key, value in result['query']['pages'].each do
	 	link= value['fullurl']
	 	#puts link
	 	f.puts(host+" "+time+" "+term+" "+ link +"\n")
	end
	}
end
	
	
     
if(ARGV.length ==0)

 
	puts"Welcome to wikipedia page of my MacBook Pro  \n \n  lets start !!! "
	puts"enter the file name in which u wanna store the logs"
	mfile=gets.chomp()

	
	ch='y';

	while (ch =="y" or ch=="Y")do
		puts "enter the term you wanna search : " 
		term=gets.chomp() 
		searchwiki(mfile,term)
		puts "do you wanna search for another term y/n"
		ch=gets.chomp()
	end
	
	puts  "EXIT"
else
	
	#puts ARGV
	searchwiki(ARGV[0],ARGV[1])
end