#reglar expression for validating nos in different scenarios
#^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$
"""
Valid Scenarios:

+91-9883443344
9883443344
09883443344
919883443344
0919883443344
+919883443344
+91-9883443344
0091-9883443344
+91 -9883443344
+91- 9883443344
+91 - 9883443344
0091 - 9883443344
7856128945
9998564723
022-24130000
080 25478965
0416-2565478
08172-268032
04512-895612
02162-240000
+91 9883443344
022-24141414
Invalid Scenarios:

WAQU9876567892
ABCD9876541212
0226-895623124
6589451235
0924645236
0222-895612
098-8956124
022-2413184
"""
t=0
while t != 1
	puts "Enter your phone no? "
	phone_no =gets.chomp

	#puts "Your no is " + phone_no +" hello"
	if phone_no=~ /(^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$)/i
		puts "Valid"
	else
		puts "Invalid"
	end
	puts "Enter 1 to stop the program"
	temp=gets.chomp
	t=temp.to_i
end













