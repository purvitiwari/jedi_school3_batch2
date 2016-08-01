#!/usr/bin/ruby -w
class IsNumber
	def isnumber(number)
		if (number =~ /^[789][0-9]{9}\b/)
			puts "standard number \n"
		elsif (number =~ /^[0][789][0-9]{9}\b/)
			puts "number with 0 leading \n"
		elsif (number =~ /^[+][9][1][789][0-9]{9}\b/)
			puts "number with +91 leading \n"
		else 
			puts "not a valid mobile number \n"
		end
	end
end
if(ARGV.length>0)
	number=ARGV[0]
	object= IsNumber. new
	object.isnumber(number)
else
	temp='yes'
	while temp=='yes' do
		puts "Please enter a number: \n";
		number = gets;
		object= IsNumber. new
		object.isnumber(number)
		puts "Do you wish to continue (yes/no): "
		temp=gets.chomp();	
	end
end