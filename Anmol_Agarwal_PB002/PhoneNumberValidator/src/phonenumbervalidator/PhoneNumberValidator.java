package phonenumbervalidator;

/**
 *
 * @author anmol
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PhoneNumberValidator {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException {
        String phoneNum;
        if(args.length > 0) {
            phoneNum = args[0];
        } else {
            System.out.println("Enter PhoneNumber:");
            BufferedReader inp = new BufferedReader(new InputStreamReader(System.in));
            phoneNum = inp.readLine();
        }
        String phoneValidator = "^(0|(\\+91))?([7,8,9])(\\d{9})";
        System.out.println("PhoneNumber '" + phoneNum + "' is " + 
                (phoneNum.matches(phoneValidator) ? "valid" : "invalid"));
    }
}
