require 'open-uri'
require "rubygems"
require "json"

$api_url = "https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&format=json&search="

class WikiSearch

	def initialize(query)
		@query = query
	end

	def searchWiki(logfile)
		logfile = open(logfile, "a")
		search_results = open($api_url + @query).read
		results = JSON.parse(search_results)
		logfile.puts " #{Time.new} #{results[0]} #{results[1]} #{results[3]} "
		return results[3]
	end
end

input_array = ARGV

if input_array.length == 1
	logfile = input_array[0]
	choice = 'y'
	while choice == 'y' or choice =='Y' do
		puts "Enter the keyword to be searched:"
		query = STDIN.gets.to_s
		puts "Searching...  #{query}"
		search_query = WikiSearch.new(query)
		search_link = search_query.searchWiki(logfile)
		puts "Search Completed..."
		puts "Link: #{search_link}"
		puts "Want to enter more queries(y/n):"
        choice = STDIN.gets.to_s.chomp
	end
else 
	logfile = input_array[input_array.length-1]
	for i in 0...(input_array.length-1)
		query = input_array[i]
		puts "Searching...  #{query}"
		search_query = WikiSearch.new(query)
		search_link = search_query.searchWiki(logfile)
		puts "Search Completed..."
		puts "Link: #{search_link}"
	end
end

