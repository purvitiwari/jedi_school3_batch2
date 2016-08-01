
################
##
#
#  PB002 CLI COMMANDS
#  Instructor  Mr. Tushar Babbar
#  Submitted By: Riya Garg
#  Emp id. P2958
#
# Phone number validator
#
##
#################


# @Description To validate the phone number use the regex of the valid phone number and validate that. only valid for the indian numbers.
#
# @param num {integer}
# @return {null}

def isvalidate(num)
	if (num =~ /^[0]{0,1}[7-9]{1}[0-9]{9}$/ )   
  		puts "valid phone number"
	elsif (num =~/^[+][9][1][7-9]{1}[0-9]{9}$/)
	  	puts "valid phone number"
    else 
	    puts "invalid phone number"
	end
end


if(ARGV.length ==0)
	
	puts "Welcome to the phone number validater \n \n This validater will only validate the number with country code of india.  \n \n lets start !!! "
 	
 	
	ch='y';

	while (ch =="y" or ch=="Y") do 
		puts "enter the phone number: " 
		num=gets
		isvalidate(num)
		puts"do you wanna enter the other number y/n"
		ch=gets.chomp()
	end
		puts  "EXIT"

else
	isvalidate(ARGV[0])
end
