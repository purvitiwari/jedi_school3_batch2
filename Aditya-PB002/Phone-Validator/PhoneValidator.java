import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*;
import java.util.Scanner;


public class PhoneValidator{

    public static void main(String[] argv) {
        String phoneNumber="";

        if (argv.length==0)
        {
             Scanner sc = new Scanner(System.in);
             System.out.println("Please enter a Number:");
             phoneNumber=sc.nextLine();
        }
        else if(argv.length>1)
        {
        	callhelp();
        }
        else
        {
        	String arg = argv[0];
        	if(arg.equals("-help") || arg.equals("-h"))
        	{
        		help();
        	}
            phoneNumber = arg;
        }   
        String regex = "^[789]\\d{9}$";// regex for Indian numbers
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(phoneNumber);

        if (matcher.matches()) 
        {
            System.out.println("Phone Number Valid");
        } 
        else 
        {
            System.out.println("The entered string is not a valid number");
        }
    }

    public static void help()
    {
    	System.out.println("This is a simple script to check if the numbers entered are in INDIAN Formats");
    	System.out.println("Please enter the numbers without the country code.For example: 9812398478");
    	System.exit(0);
    }

    public static void callhelp()
    {
    	System.out.println("Invalid number of arguments entered.Please type -h or -help as the first argument"
 							+ " to get help!");
    	System.exit(0);
    }
}