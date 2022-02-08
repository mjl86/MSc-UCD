package ma4;
import java.io.File;

import java.util.Date;
public class Q2 {
	public static void main(String [] args) {
		// Create a File instance from argument file
		File file = new File(args[0]);
		
		//create a boolean to test if the file exists
		boolean exists=file.exists();
		//Prints if the file exists
		System.out.println("File exists: " + exists);
		//if the file exists
		if (exists== true);{
			Date date=new Date();
			//convert the date to a string
			String d=date.toString();
			//remove whitespace
			String d2 = d.replace(" ", "");
			//remove the colons
			String d3 = d2.replace(":", "");
			// initalise new variable with new file name
			File newFile= new File(args[0] + d3);
			//rename file
			boolean b = file.renameTo(newFile);
			//print new file name
			System.out.println(newFile);
			//if renamed successfully prints true otherwise prints false
			System.out.println(b);
			
		}
	}
}
