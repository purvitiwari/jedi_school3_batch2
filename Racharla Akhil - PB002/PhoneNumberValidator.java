import java.util.Scanner;

public class PhoneNumberValidator {
	public static void main(String[] args) {
		String phoneNumber;
		if(args.length > 0) {
			phoneNumber = args[0];
		} else {
			Scanner input = new Scanner(System.in);
			System.out.println("Enter Phone number");
			phoneNumber = input.nextLine();
			input.close();
		}
		
		String regex = "^((0)|(\\+91))?([7,8,9])(\\d{9})";
		System.out.println(phoneNumber +  " is " + (phoneNumber.matches(regex) ? ("valid") : "invalid") + " phone number.");
	}
}
