package ma1;
//program to tell the number of days in a given month including leap years
import java.util.Scanner;
public class Q2 {

	public static void main(String[] args) {
		//user input
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the year and month: ");
		//reads the input
		int year = input.nextInt();
		int month = input.nextInt();
		input.close();
		//main body that tells how many days are in each month.
		switch (month) {
		  case 1:
		    System.out.println("There are 31 days in January");
		    break;
		  case 2:
			  //computes if the year is a leap year when February is selected to see if its 28 or 29 days long
			  if ( year % 4 == 0 && year % 100 !=0 || year % 400 == 0) {
					System.out.println("It's a leap year.There are 29 days in Febuary");
				}else {
		    System.out.println("There are 28 days in Febuary");
		    }
		    break;
		  case 3:
		    System.out.println("There are 31 days in March");
		    break;
		  case 4:
		    System.out.println("There are 30 days in April");
		    break;
		  case 5:
		    System.out.println("There are 31 days in May");
		    break;
		  case 6:
		    System.out.println("There are 30 days in June");
		    break;
		  case 7:
		    System.out.println("There are 31 days in July");
		    break;
		  case 8:
			System.out.println("There are 31 days in August");
			break;
		  case 9:
		    System.out.println("There are 30 days in September");
			break;
		  case 10:
			System.out.println("There are 31 days in October");
			break;
		  case 11:
			System.out.println("There are 30 days in November");
			break;
		  case 12:
			  System.out.println("There are 31 days in December");
		  default:
			  System.out.println("Month must be an integer between 1 and 12 inclusive.");
		}
		

	}

}
