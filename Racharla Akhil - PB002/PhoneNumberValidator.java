import java.util.Scanner;

public class PhoneNumberValidator {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while(true) {
			System.out.println("Enter Phone number");
			String phoneNumber = input.nextLine();
			String regex = "^((0)|(\\+91))?([7,8,9])(\\d{9})";
			System.out.println(phoneNumber +  " is " + (phoneNumber.matches(regex) ? ("valid") : "invalid") + " phone number.");
		}
	}
}
