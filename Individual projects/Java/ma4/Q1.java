package ma4;
// a program to read in a file and count the number of lines, characters and words.
import java.io.*;

public class Q1 {
	public static void main(String [] args){
		try {
			//reading in file as argument from the command line
			File file = new File(args[0]);
			BufferedReader in = new BufferedReader(new FileReader(file));
			String line;
			//initalising count variables
			int charCount=0;
			int wordCount=0;
			int lineCount=0;
			//while loop that instantiates line so long as in is not equal to 0.
			while ((line = in.readLine()) !=null) {
				// if the line is not equal to a space count it as a character and increase charCount
				if (line != "\s") {
						charCount+=line.length();
				}
				
				//makes a string array that splits the words at spaces and add them to the array increase wordCount by array length.
				if (line != "\s" || line != "\n") {
				String [] words=line.split(" ");
				wordCount += words.length;
				}
				// increments the linecounter
				lineCount ++;
				
					
				}
			// print the counts	
			System.out.println("There are " + charCount + " characters in the file");
			System.out.println("There are " + wordCount + " words in the file");
			System.out.println("There are " + lineCount + " lines in the file");
			in.close();
			//exception catch for input output
		} catch (IOException ex) {
			ex.printStackTrace();
		}
		}
}
	

