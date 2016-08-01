require 'net/http'
require 'json'
def searcher(tosearch,tostore)
	response = Net::HTTP.get_response(URI.parse("https://en.wikipedia.org/w/api.php?action=opensearch&search="+tosearch+"&limit=1&format=json"))
	data=response.body
	data=JSON.parse(data)
	puts "\nTitle of the page you had requested : "+data[1][0]
	puts "\nUrl of the page you had requested : "+data[3][0]
return data[3][0]
end
if ARGV.length>=2
	tosearch=ARGV.second.to_s
	tostore=ARGV.first.to_s
elsif ARGV.length==1
	tostore=ARGV.first
	puts "Please Enter a string to be searched\nover wikipedia"
	tosearch=STDIN.gets
else
	puts "Please Enter where you want to be store log"
	tostore=STDIN.gets
	puts "Please Enter a string to be searched\nover wikipedia"
	tosearch=STDIN.gets
end

f=File.open(tostore, 'w')
data=searcher(tosearch,tostore)
f.write(tosearch+"resulted to "+data+"\n") 
puts "Press one of the following:\n1 to search again\n2 to exit:"
check=STDIN.gets.to_i
while(check!=2)
puts "Please Enter a string to be searched\nover wikipedia"
tosearch=STDIN.gets

data=searcher(tosearch,tostore)
f.write(tosearch+"resulted to "+data+"\n") 
puts "Press one of the following:\n1 to search again\n2 to exit:"
check=STDIN.gets.to_i
end



