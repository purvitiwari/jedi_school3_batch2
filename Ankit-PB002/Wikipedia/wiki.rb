require 'wikipedia'
require 'socket'
puts "Please enter Article Name: "
article= gets
time = Time.now
time=time.strftime("%Y-%m-%d %H:%M:%S")
host = UDPSocket.open {|s| s.connect("64.233.187.99", 1); s.addr.last}
puts host
page = Wikipedia.find(article)
puts page.fullurl
open('wiki.log', 'a') { |f|
  f.puts (host+" "+time+" "+page.title+" "+page.fullurl)
}