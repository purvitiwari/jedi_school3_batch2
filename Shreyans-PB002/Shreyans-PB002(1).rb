def validate(str)
	if str =~ /^[7-9][0-9]{9}$/ or str =~ /^[+][9][1][7-9][0-9]{9}$/ or str =~/^0[7-9][0-9]{9}$/
		return "Valid\n"
	else
		return "Invalid\n"
	end
end
$number = ARGV
if $number.length == 0
	$num = ''
	while not ($num =='q' or $num =='Q') do
		puts "Enter Number to Validate or q to exit:"
		$num = gets.chomp()
		if not ($num =='q' or $num =='Q')
			puts validate($num)
		else
			puts "Program Exiting"
		end
	end
else
	for $numbr in $number
		puts $numbr+" is "+validate($numbr)
	end
end
