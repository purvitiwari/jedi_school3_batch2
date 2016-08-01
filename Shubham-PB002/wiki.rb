require 'rubygems'
require 'json'
require 'net/http'
require 'optparse'

def log(url, logFile)
  open(logFile, 'a') { |f|
    f.puts url
  }
end

def searchWiki(term, logFile)
  puts "Searching for \"" + term + "\" ..."
  
  response = Net::HTTP.get_response(URI.parse(
    'https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search=' + URI::encode(term)))
  json = JSON.parse(response.body)
  puts json[1], "\n", json[2], "\n", json[3], "\n"
  
  log(json[3], logFile)
  
end

if(ARGV.length != 2)
  puts "Usage: ruby wiki.rb [search term] [log file name]"
  exit 1
end

searchWiki(ARGV[0], ARGV[1])