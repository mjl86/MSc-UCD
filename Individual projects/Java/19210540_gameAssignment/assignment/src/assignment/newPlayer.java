package assignment;

import java.time.LocalDateTime; // Import the LocalDateTime class
import java.time.format.DateTimeFormatter; // Import the DateTimeFormatter class

// class to define new players

public class newPlayer {
	//initialise private class variables
	private String name;
	private static int points;
	//constructor with parameters
	public newPlayer(String name,int points) {
		this.name=name;
		newPlayer.points=0;
	}
	//no parameters constructor
	public newPlayer() {
		this("newplayer",0);
	}
	//getters and setters for the private variables
	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name=name;
		
	}

	public static int getPoints() {
		return newPlayer.points;
	}

	public static void setPoints(int points) {
		newPlayer.points = points;
		points=getPoints()+1;
	}
	// an override to string method for the newplayer class
	public String toString() {
		
		LocalDateTime myDateObj = LocalDateTime.now(); 
		DateTimeFormatter myFormatObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
		String formattedDate = myDateObj.format(myFormatObj); 
		String result="\n" + getPoints() + "\t\t" + name  + "\t\t " + formattedDate;
		return result;
	}
		
}


