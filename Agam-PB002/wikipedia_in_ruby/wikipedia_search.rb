require 'wikipedia'
# page=Wikipedia.find("albert")
# puts page[0].fullurl
# puts page.summary
i=0
file_name=open("result.log","a")
while i !=1
	puts "Enter the name "
	name =gets.chomp
	page=Wikipedia.find(name)
	link=page.fullurl
	puts link
	file_name.write("Name= "+name+"  Link= "+link+"\n \n")
	puts "Enter 1 to stop"
	
	temp=gets.chomp
	i=temp.to_i
end
