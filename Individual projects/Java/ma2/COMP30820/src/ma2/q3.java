package ma2;
import java.util.Scanner;

//program to calculate the number of points based on games won lost or drawn and game average.
public class q3 {
	public static void main(String[] args) {
	
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a string representing and number of wins,draws and losses. e.g.WWDL");
		String results= input.next();
		double wins=0;
		double draws=0;
		
		//tests the letters entered and increments the wins or draws counter if one of the characters is a w or d.
		//if another character is found it prints invalid.
		for (int i = 0; i < results.length(); i++) {
			if (!results.matches("[wdlWDL]+")){
				System.out.println("Invalid input.Try again.");
				
			}
			if (results.charAt(i) == 'w' || results.charAt(i)== 'W'){
				wins+=1;
			}
			else if (results.charAt(i) == 'd' || results.charAt(i)== 'D'){
				draws+=1;
			}
			
			
			input.close();
			
		}
		//calculates the points based on w and d's entered and calculates the average and prints the results 
		double winner=wins*3;
		double nowinner=draws*1;
		double total=winner+nowinner;
		double average=total/results.length();
		System.out.println("Total points " + total);
		System.out.println("Average points " + average);
		
	}

}
