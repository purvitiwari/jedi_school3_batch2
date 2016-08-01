$choice = 'y'

class Validator
    def initialize(number)
    	@number = number
    end
    def validateNumber
    	if (@number =~ /^[7-9][0-9]{9}\b/) or (@number =~ /^[0][7-9][0-9]{9}\b/) or (@number =~ /^[+][9][1][7-9][0-9]{9}\b/)
    	    "is valid"
    	else 
    		"is not valid"
    	end3
    end
end

input_numbers = ARGV
no_of_args = input_numbers.length

if no_of_args == 0
    while $choice == 'y' or $choice == 'Y' do
        puts "Enter number"
        num = gets.chomp()
        isvalid = Validator.new(num)
        puts "#{num} #{isvalid.validateNumber()}"
        puts "Want to enter more numbers(y/n):"
        $choice = gets.chomp()
    end
else
    for i in 0...no_of_args
        num = ARGV[i].chomp()
        isvalid = Validator.new(num)
        puts "#{num} #{isvalid.validateNumber()}"
    end
end

