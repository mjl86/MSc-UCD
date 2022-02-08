package assignment;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class leaderBoard {
		
	public static void leader() throws Exception{
	
		// reading in the text file where the leader board scores are saved to.
		FileReader fileReader = new FileReader("C:\\Users\\maria\\workspace-Comp30820exam\\assignment\\leaderBoard.txt");
		BufferedReader bufferedReader = new BufferedReader(fileReader);
		String inputLine;
		//create a list of strings to hold the leader board text file read in above.
		List<String> lineList = new ArrayList<String>();
		while ((inputLine = bufferedReader.readLine()) != null) {
			lineList.add(inputLine);
		}
		fileReader.close();
		//sorts the list linelist in descending order by points.
		Collections.sort(lineList,Collections.reverseOrder());
		
		System.out.printf("\t\t----LeaderBoard----\n");
		System.out.printf("POINTS \t\t NAME \t\t DATE \n");
		//loop that displays the sorted leader board on exiting main menu when this class is called.
		for (String outputLine : lineList) {
			System.out.println(outputLine);
		}
		
		

	}
}
