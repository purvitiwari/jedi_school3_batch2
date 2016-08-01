//            Documentation 

// This Code the Validate weather given Phone number is valid or not

// Input formate PhoneNumberValidator [Phone number]

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;

public class PhoneNumberValidator
{
    public static void main( String  args[]){
      String phonenumber = "";
      int var = args.length;
      if (var > 0){
         phonenumber = args[0];
      }
      else{
         System.out.println("Enter Phone Number: ");
         Scanner scanner = new Scanner(System.in);
         phonenumber = scanner.nextLine();
      }
      String pattern = "^([0]|\\+91)?[789]\\d{9}$";
      Pattern r = Pattern.compile(pattern);
      Matcher m = r.matcher(phonenumber);
      if (m.find( )) {
         System.out.println("Valid Phone Number");
      } else {
         System.out.println("NOT Valid Phone Number");
      }
   }
}