
package assignment;
import java.util.Random;
import java.util.Scanner;
import java.lang.Math;

public class game extends newPlayer{
	//Game 1 Rock paper scissors
	public static void rockPaperScissors(){
		Random rnd = new Random();
		int i = 0;
		String[] rps= {"rock", "paper","scissors"};
		Scanner input= new Scanner(System.in);
		
		//A do while loop that allows the player to play three rounds of rock paper scissors.
		//rock beats scissors, scissors beat paper, paper beats rock
		//10 points for a win, 5 points for a draw and 0 points for a loss.
		
		do {
		// the computer makes it's choice by randomly selecting an index of one of the values in the array rps.	
		int rand=rnd.nextInt(rps.length);
		// asks for the players guess
		System.out.printf("Enter rock, paper or scissors:");
		String guess=input.nextLine();
		//The computers choice
		System.out.printf("The Computer selected: " + rps[rand]+ "%n");
    
		//win scenarios
	    if (guess.equals("rock") && rps[rand].equals("scissors")) {
			setPoints(getPoints()+ 10);
			System.out.printf("You win 10 points%n%n" );
		}
	    else if (guess.equals("scissors") && rps[rand].equals("paper")) {
	    	 System.out.printf("You win 10 points%n%n");
			setPoints(getPoints()+ 10);
			 System.out.printf("You win 10 points%n%n");
		}
	   
	    else if (guess.equals("paper") && rps[rand].equals("rock")) {
			setPoints(getPoints()+ 10);
			 System.out.printf("You win 10 points%n%n" );
		}
	    
	    //draw scenarios
	    else if (guess.equals("rock") && rps[rand].equals("rock")) {
			setPoints(getPoints()+ 5);
			 System.out.printf("It's a draw! You get 5 points.%n%n");
		}
		else if (guess.equals("paper") && rps[rand].equals("paper")) {
			setPoints(getPoints()+5);
			 System.out.printf("It's a draw! You get 5 points.%n%n");
		}
		else if (guess.equals("scissors") && rps[rand].equals("scissors")) {
			setPoints(getPoints()+ 5);
			System.out.printf("It's a draw! You get 5 points.%n%n");
		}
		//lose scenarios
		else if ( guess.equals("rock") && rps[rand].equals("paper")) {
				 System.out.printf("Sorry! No points.%n%n");
			}
		 else if ( guess.equals("scissors") && rps[rand].equals("rock")) {
				 System.out.printf("Sorry! No points.%n%n");
			}
		 else if ( guess.equals("paper") && rps[rand].equals("scissors")) {
				 System.out.printf("Sorry! No points.%n%n");
			}
	    
	
		  i++;
	    }
		
		while(i<3);
		
		//Conditions on what the player sees depending on points won in the game.
		if (getPoints()==0) {
			System.out.printf("Better luck next time! You won " + getPoints() + " points.%n");
			}
			else {
				System.out.printf("Congratulations! You won " + getPoints() + " points.%n");
			}
		System.out.printf("----------GAME OVER----------%n%n");

	
		
}
	
	
	
// Game 2 Guess the number between 1-20
	public static void numberGuess() {
		// print game name
		System.out.printf("***** Random Guess *****%n%n");
		// Initialise variables
		int i=0;
		int max=20;
		int min = 0;
		int number;
		int range = max - min +1;
		// computes a random number
		int rand= (int)Math.floor(Math.random() * range)+min;
		Scanner input= new Scanner(System.in);
		
		//do while loop allows the player three guesses if they guess correct the number changes or else they have the chance to guess the number 3 times.
		do {
			System.out.println(rand);
		System.out.println("Guess the number between 0-20");
		number=input.nextInt();
		
		if (rand == number){
			rand= (int)Math.floor(Math.random() * range)+min;
			setPoints(getPoints()+15);
			System.out.printf("You won 15 points.%n%n");
		}
	
		//if the guess is incorrect hints of higher or lower than their guess are given to help the player
		else if (rand != number && rand > number) {
			System.out.printf("The number is higher.%n%n");
			}
		else {
				System.out.printf("The number is lower.%n%n");
			}
		// increments i for the while condition below.	
		i++;
		
		}
		while (i < 3 );
		
		
		//Conditions on what the player sees depending on points won in the game.
		if (getPoints()==0) {
		System.out.printf("Better luck next time! You won " + getPoints() + " points.%n");
		}
		else {
			System.out.printf("Congratulations! You won a total of " + getPoints() + " points.%n");
		}
		System.out.printf("----------GAME OVER----------%n%n");
		
}
	
}
