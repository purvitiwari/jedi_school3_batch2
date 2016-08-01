require 'net/http'
require 'uri'
require 'json'



def getSearchResult(api_url,query)
	payload = { :action => 'opensearch', :search => query,
				:limit => 1, :format => 'json'}
	uri = URI(api_url)
	uri.query = URI.encode_www_form(payload)
	
	begin
		res = Net::HTTP.get_response(uri)
		
		jsonRes = JSON.parse(res.body)
		jsonRes
	rescue Timeout::Error, Errno::EINVAL, Errno::ECONNRESET, EOFError,
       Net::HTTPBadResponse, Net::HTTPHeaderSyntaxError, 
       Net::ProtocolError, SocketError => e
       puts e
       nil
   end
end





def saveLogToFile(logFile, query, data)
	title = data[1][0]
	url = data[3][0]
	dataDump = "{'Query' : "+query+", 'Title' : "+title+
				", 'URL' : "+url+"}"
	logFile.puts dataDump
end


api_url = 'https://en.wikipedia.org/w/api.php'
query = ''

# Handling command Line arguments
if(ARGV.length !=1 && ARGV.length !=2)
	puts "Usage : #{$0} filename [query]"
	exit
end


filename = ARGV[0]
logFile = File.open(filename,'a')
if(logFile == nil)
	puts "Unable to open a file"
	exit
end

if(ARGV[1]!=nil)
	query = ARGV[1]
else
	puts "Enter a query to search for: "
	query = STDIN.gets.to_s
	query = query.chomp
end

while query != "e" && query != "q" do
	puts "querying to Wikipedia...."
	result = getSearchResult(api_url,query)
	puts "Done\n"

	if (result == nil || result[3] == nil || result[3] == [])
		puts "Something Went wrong "
		puts "Terminating program.................."
		break
	else
		puts "Saving to log File"
		saveLogToFile(logFile, query, result)
		puts "Done\n"
		puts "Enter another query to search for or type q or e to exit: "
		query = STDIN.gets.to_s
		query = query.chomp
	end
end
logFile.close

