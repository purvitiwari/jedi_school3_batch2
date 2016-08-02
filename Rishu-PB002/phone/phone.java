import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*;
import java.util.Scanner;


public class phone{

    public static void main(String[] argv) {
        String phoneNumber;

        if (argv.length==0){
             Scanner sc = new Scanner(System.in);
             System.out.println("Please enter a Number :");
             phoneNumber=sc.nextLine();
        }
        else{
            phoneNumber = argv[0];
        }   
        System.out.println(phoneNumber);
        // regex for Indian numbers
        String regex = "^(((\\+|00)\\d{1,3}[\\s-]?)|0)?\\d{10}$";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(phoneNumber);

        if (matcher.matches()) {
            System.out.println("Phone Number Valid");
        } else {
            System.out.println("Phone Number must be in the indian format");
        }
    }
}