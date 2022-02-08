package ma1;
import java.util.Scanner;
public class Q1 {
// Program to estimate the length of runway needed given an aircrafts acceleration and speed with a 15% increase if the runway is wet.
	public static void main(String[] args) {
		//Gets the user's input (acceleration rate (a), speed (v) and runway condition wet(w) or dry(d)
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the airplane's acceleration, speed and runway condition: ");
		
		//reads the user input
		double a = input.nextDouble();
		double v = input.nextDouble();
		char ch = input.next().charAt(0);
		
		//runway length formula for dry runway
		double length = Math.pow(v,2)/(2*a);
		
		//Calculates the runway length based on it being wet and adds 15% to calculation.
		if (ch == 'w' || ch=='W') {
			System.out.println("The runway is wet");
			double l= length*0.15; 
			double wetLength= l + length;
			System.out.println("The length of the runway needed is:" + wetLength);
		}
		else if (ch=='d' || ch=='D'){
			System.out.println("The runway is dry");
			System.out.println("The length of the runway needed is:" + length);
		}else {
			System.out.println(ch + " is not a valid input. Enter eith w for wet or d for dry runway conditions.");
		}
	
		
		
		input.close();
		

	}

}
