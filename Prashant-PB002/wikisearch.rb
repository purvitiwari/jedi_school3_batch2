#! /usr/bin/env ruby

require 'slop'
require 'wikipedia'

opts = Slop.parse do |o|
  o.string '-s', '--search', 'search term', default: ''
  o.string '--log-file', 'log results to this file (default: wiki.log)', default: 'wiki.log'
  o.bool '-h', '--help', 'show this help'
end

if opts.help?
  puts opts
  exit
end

log_file =  opts[:log_file]

if opts[:search].empty?
  print "Enter search term: "
  search_term = STDIN.gets.chomp
else
  search_term = opts[:search]
end

page = Wikipedia.find(search_term)

# Page does not exist if == '-1'
if page.raw_data['query']['pages'].first[0] == '-1'
  STDERR.puts "No wikipedia article found for '#{search_term}'"
else
  puts page.fullurl
  File.open(log_file, 'a') { |f| f.puts page.fullurl }
end
