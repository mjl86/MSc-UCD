package ma2;

import java.util.Scanner;

// Program to calculate the future value of an investment given an annual interest rate and amount to invest.
public class q1 {
	static double interest;
	//Main method reads in the investment amount an interest and prints the value at each year invested from 1-30 years.
	public static void main(String[] args) {
		int years=0;
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the amount to invest:");
		double money= input.nextDouble();
		System.out.println("Enter the interest rate:");
		interest=input.nextDouble();
		System.out.println();
		input.close();
		//error checking to ensure numbers entered are not negative
		if (money <0 || interest<0) {
			System.out.println("Amount and interest should not be negative");
		}else {
			while (years <30) {
				years++;
				System.out.print(years + "\t");
				//calling the futureValue method to calculate the investment amount 
				System.out.println(String.format("%.2f",futureValue(money,interest,years)));

			}
		}
	}
	//method to calculate the future value of the investment aount
	
	public static double futureValue(double amount, double monthlyRate,int years) {
		monthlyRate=interest/1200.0;
		double investment = amount * Math.pow(1.0+ monthlyRate,years*12);
		return (investment);
		
		
	}

}
