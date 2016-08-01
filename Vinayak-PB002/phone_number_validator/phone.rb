phone_number = ""
if ARGV.length == 0
	puts "Enter phone number :"
	phone_number = gets.chomp
	puts phone_number
else
	phone_number = ARGV[0]
	puts phone_number
end
VALID_PHONE_NUMBER_REGEX = /\A([0]|(\+91))?[789]\d{9}\Z/
if VALID_PHONE_NUMBER_REGEX =~ phone_number
	puts "Valid phone Number!"
else
	puts "Invalid phone number!"
end