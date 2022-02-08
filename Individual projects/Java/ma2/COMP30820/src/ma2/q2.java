package ma2;

import java.util.Scanner;
//Program to create a password that must comply with these three rules.
public class q2 {
	static String password;
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a password:");
		password= input.nextLine();
		if (tenchars(password)==true && lettersDigits(password)==true && threeDigits(password)==true) {
			System.out.println("Valid Password");
		}
		else {
			System.out.println("Invalid Password");
		}
	input.close();
}
	
	//tests to see if password is longer than 10 characters returns true if it is.
	public static boolean tenchars(String password) {
		if (password.length()< 10) {
			return false;
		}else {
			return true;
			}
		}
	
	//tests to see if it only contains lower and upper case letters and numbers returns true if it does
	public static boolean lettersDigits(String password){
		if (password.matches("[a-zA-Z0-9]+")) {
			return true;
		}else {
			return false;
			}
		}
	//tests to see if the password contains three or more numbers returns true if it does.
	public static boolean threeDigits(String password) {
			int count=0;
			for (int i=0; i<password.length();i++) {
				if(Character.isDigit(password.charAt(i))) {
					count++;
					}
				}
			if (count >= 3) {
				return true;
				}else {
					return false;
			}
		}
			
		
				
			}
	
	

	
