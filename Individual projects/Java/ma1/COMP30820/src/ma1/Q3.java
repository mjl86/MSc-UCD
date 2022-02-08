package ma1;
//Program to generate a random number and asks you to guess what number has been generated between 0-100 inclusive.
import java.util.Scanner;
public class Q3 {
	public static void main(String[] args) {
		System.out.println("Guess a number from 0-100");
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a number:");
		//variables
		int min = 0;
		int max = 100;
		double rd = Math.random();
		//converts the Math.random method to an int x and multiplies it by the max number - min and adds one so that 100 is included 
		int x = min + (int)(rd * (max-min)) + 1;
		//initials number
		int number1=0;
		//while loop that continues asking for user input until the right number is entered then the loop exits.
		while (number1 != x) {
			int number2 = input.nextInt();
			if (number2 > x) {
				System.out.println("Too high");
			}
			else if (number2 < x){
				System.out.println("Too low");
			} else {
				System.out.println(x + " is correct");
			}
		}
		
		input.close();
	}

}
