require 'net/http'
require 'uri'
require 'json'

puts "Please enter the keyword to search: "
A = gets.strip
A.sub!(" ","%20")
# puts A

print "Requesting the Wekipedia Servers. Hold On...................."
url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&search="+A+"&language=en&limit=20&format=json" # trailing slash is important
uri = URI.parse(url)

results = Net::HTTP.get(uri) # GET request

############  json data returned from HTTP get request
jsonData =  JSON.parse(results)
puts jsonData
############  If response has any valid result
if(jsonData.key?("search"))
	#puts jsonData["search"][0]["url"]
	if(jsonData["search"].any?)
		open('log.txt', 'a') { |f|
		  urlS = jsonData["search"][0]["url"]
		  timeStamp = Time.now.strftime("%Y-%m-%d %H:%M:%S")
		  f.puts urlS  +"	"+timeStamp+"\n"
		}
	else
		puts "\nNo Matching results were found."
	end
else
	puts "\nNo results are found."
end

