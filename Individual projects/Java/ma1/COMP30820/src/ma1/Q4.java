package ma1;
// a program to find the longest common prefix of two strings
import java.util.Scanner;
public class Q4 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter two strings:");
		String strA = input.nextLine();
		String strB = input.nextLine();
		int minLength= Math.min(strA.length(),strB.length());
		int count=0;
		
		// a while loop that increments a count by one and while it is less or equal than the minimum length of the two strings keeps looping
		while (count<= minLength) {
			count++;
			// if the first character of each loop are not equal then  there's no common prefix
			if (strA.charAt(0)!=strB.charAt(0)) {
					System.out.println("no common prefix");
			}
			//if the characters at each count are equal and string a is less than or equal to minimum length print strA else print strB
			//Issue here i could not solve is that if the strings are the same length and the last characters are not equal it'll still print out all of strA 
			else if ((strA.charAt(count)==strB.charAt(count))) {
				if (strA.length() <= minLength) {
					System.out.println(strA);
					}
				else {
					System.out.println(strB);
					}
			}
			//breaks the loop if the conditions are satisfied and ensures the answer is only printed once
		break;
		}
		
		input.close();
	}
}

		




	
	

	





