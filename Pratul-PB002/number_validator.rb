#Phone number validator

def is_valid(number)
	if (number =~ /\A([0]|(\+91))?[789]\d{9}\Z/)
		return true
	else
		return false
	end
end


number = ""
if ARGV.length == 0
	puts "Enter phone number :"
	number = gets.chomp
else
	number = ARGV[0]
end
if (is_valid(number))
	puts "Valid number"
else
	puts "Invalid number"
end
