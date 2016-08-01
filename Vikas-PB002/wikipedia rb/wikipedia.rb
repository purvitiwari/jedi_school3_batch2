#!/usr/bin/ruby
require 'wikipedia'
require 'socket'

logfile = open("wikipedia.log", "a")
flag = "true"
numb = 1;
while(flag=="true") do
	puts "enter any name you want to search"
	name = gets
	time= Time.now
	time=time.strftime('%Y-%m-%d %H:%M:%S')
	host = UDPSocket.open {|s| s.connect("64.233.187.99", 1); s.addr.last}
	puts host
	page = Wikipedia.find( name )
	url = page.fullurl
	puts url

	logfile.puts(host+ " "+ time+" " +page.title+" "+ page.fullurl)

	puts "Do You Want To Continue, (yes or no) "
	numb = gets.chomp()
	if 	(numb == 'no')
		flag = "false"
	
	else(numb == 'yes')
		flag = "true"
	end
end
