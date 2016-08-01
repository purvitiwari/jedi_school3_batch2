import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class phoneNumber {

    public static void check_validity(String number){
        String regex = "^(0|\\+91)?[789]\\d{9}$";
            Pattern pattern = Pattern.compile(regex);
            Matcher matcher = pattern.matcher(number);

            if (matcher.matches()) {
                System.out.println("Phone Number Valid");
            } else {
                System.out.println("Phone Number not valid");
            }
    }

    public static void main(String[] argv) {

        Scanner input = new Scanner(System.in);
        String number = "";
        
        if(argv.length > 1)
        {
            for(int i=0;i<argv.length;i++)
                check_validity(argv[0]);
        }
        
        while(true)
        {
            number = "";
            while (number.equals(""))
            {
                System.out.print("Enter mobile number or 'exit' to quit: ");
                number = input.nextLine();
                if(number.equals("exit"))
                {
                    return;
                }
            }
            check_validity(number);
            
        }
    }
}