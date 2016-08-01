#!/usr/bin/ruby

flag= "true";
numb = 1;
while(flag=="true") do
	puts "enter any phone number"
	num = gets
		if (num =~ /^[0][7-9]{1}[0-9]{9}$/ )
			puts "Yes, It is a valid number starting with 0"

		elsif (num =~ /^[7-9]{1}[0-9]{9}$/)  
			puts "Yes, It is a valid number"

		elsif (num =~ /^[+][9][1][7-9]{1}[0-9]{9}$/)
			puts "Yes , It is a valid number starting with +91"
		else
			puts "No, It is not a valid number"
		end  
	puts "Do You Want To Continue, (yes or no) "
	numb = gets.chomp()
	if 	(numb == 'no')
		flag = "false"
	
	else(numb == 'yes')
		flag = "true"
	end
end



