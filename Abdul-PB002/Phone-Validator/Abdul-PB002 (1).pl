use strict;

if ( @ARGV >1){
	print "Usage: perl $0 [Phone Number|--help|-h]\n\n";
	exit;
}

if( $ARGV[0] eq "--help" || $ARGV[0] eq "-h"){
	print "Usage: perl $0 [Phone Number|--help|-h]\n\n";
	exit;
}

print "Welcome to Phone Number Validator\n";
print "This program validates the Indian phone number. So let's Begin\n";

my $phone_no="";

if( @ARGV == 1){
	$phone_no = $ARGV[0];
	print "You have passed $phone_no as the argument\n";
} 
else{
	print "\nEnter a phone number \:\$ ";
	chomp( $phone_no=<STDIN>);
}
# print "$phone_no";
while ($phone_no ne "exit" && $phone_no ne "quit" && $phone_no ne "q" && $phone_no ne "e"){

	if ($phone_no =~ /^((\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$/)
	{
		print "\n$phone_no is a Valid Phone Number for India\n\n";
	} 
	else{
		print "\n$phone_no is an Invalid Phone Number for India\n\n";
	}
	print "Would you like to try another Number(Type exit or quit to terminate) \:\$ ";
	chomp($phone_no = <STDIN>);
}
