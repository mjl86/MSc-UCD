package assignment;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class test {
	public static void main (String args[]) throws Exception {
		int number;
		
		String name;
		System.out.printf("----Main Menu---- %nPlease choose an option 1 or 2 & press enter: %n 1. New PLayer %n 2. Quit %n");
		Scanner input= new Scanner(System.in);
		number=input.nextInt();
	//if 1 is selected the player is prompted for their name and asked to chose a game.
		if (number==1) {
			System.out.println("Please enter your name:");
			name = input.next();
			 //creates a new player instance
			
			newPlayer player= new newPlayer(name,0);
			System.out.printf("----Game Menu---- %n Hello " + player.getName() + " Please choose a game, or -1 to quit and save: %n%n 1. Rock Paper Scissors %n 2. Random Guess %n");
			// first while loop while the number is not -1 the exit command.
			while (number != -1) {
				number=input.nextInt();
				//if one is enter rock paper scissors is selected
				if (number == 1) {
					game.rockPaperScissors();
					
					System.out.printf("----Game Menu---- %n Hello " + player.getName() + " Please choose a game, or -1 to quit and save: %n 1. Rock Paper Scissors %n 2. Random Guess %n");
				}
				//else if 2 is selected play number guess
				else if (number == 2) {
					game.numberGuess();
					
					System.out.printf("----Game Menu---- %n Hello " + player.getName() + " Please choose a game, or -1 to quit and save: %n 1. Rock Paper Scissors %n 2. Random Guess %n");
				}
				//if number =-1 exit to main menu and save the points to the leader board 
				else if (number==-1){
					try {
						FileWriter f = new FileWriter("leaderBoard.txt",true);
							    
							    // write object to file
							   f.write(player.toString());
							   f.close();

							} catch (IOException ex) {
							    ex.printStackTrace();
							}
				}
				
				
			}
			
			System.out.printf("----Main Menu---- %nPlease choose an option: %n 1. New PLayer %n 2. Quit %n");
		}else if (number==2){
		// Displays leader board
			leaderBoard.leader();
			
		}
		//While the number is not 2 in main menu enter the loop the same as above but will keep repeating.
		while( number !=2) {
			number=input.nextInt();
			if (number==1) {
				System.out.println("Please enter your name:");
				name = input.next();
				newPlayer player= new newPlayer(name,0);
				 //creates a new player instance
				player.setName(name);
				System.out.printf("Hello " + player.getName() + "----Game Menu---- %n Please choose a game, or -1 to quit and save: %n 1. Rock Paper Scissors %n 2. Random Guess %n");
				// will keep looping until the player chooses to exit by entering -1
				while (number != -1) {
					number=input.nextInt();
					if (number == 1) {
						game.rockPaperScissors();
						
						System.out.printf("Hello " + player.getName() + "----Game Menu---- %n Please choose a game, or -1 to quit and save: %n 1. Rock Paper Scissors %n 2. Random Guess %n");
					}
					else if ( number == 2) {
						game.numberGuess();
						
						System.out.printf("Hello " + player.getName() + "----Game Menu---- %n Please choose a game, or -1 to quit and save: %n 1. Rock Paper Scissors %n 2. Random Guess %n");
					}
					else {
						try {
							FileWriter f = new FileWriter("leaderBoard.txt",true);
								    
								    // write object to file
								   f.write(player.toString());
								   f.close();

								} catch (IOException ex) {
								    ex.printStackTrace();
								}
					}
					
				
					
				}	
				System.out.printf("----Main Menu---- %n Please choose an option: %n 1. New PLayer %n 2. Quit %n");
			}else if (number==2){
			
				leaderBoard.leader();
			}
			
			
			
			}
			input.close();
			}
}

