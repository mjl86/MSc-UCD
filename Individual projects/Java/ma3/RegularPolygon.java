package ma3;
// Program to create Polygon objects


//creating class with private data fields n and length
public class RegularPolygon {
	private int n=3;
	private double length=1;
	// no arg constructor that creates polygon with default n and length values
	public RegularPolygon() {
		
	}
//constructor that creates a regular polygon with defined length and side
	public RegularPolygon(int n, double length) {
		this.n=n;
		this.length=length;
	}
//getter for n value
	public int getN() {
		return this.n;
	}

//getter for length value
	public double getLength() {
		return this.length;
	}
//setter for n value	
	public void setN(int newN) {
		//condition to make sure n is a positive integer
		if (newN < 1) {
			System.out.println("N must be a positive integer");
		}else {
			this.n=newN;
		}
		
	}
// setter for length value	
	public void setLength(double newLength) {
		if (newLength < 1) {
			System.out.println("Number of sides must be a positive integer");
		}else {
			this.length=newLength;
		}
		
	}
// method to calculate the perimeter of the polygon
	public static double getPerimeter(RegularPolygon obj) {
		double perimeter=obj.n*obj.length;
		System.out.println("The perimeter is:" + perimeter);
		return perimeter;
	}
// method to calculate the area of the polygon	
	public static double getArea(RegularPolygon obj) {
		double area= (obj.n*Math.pow(obj.length,2))/(4*Math.tan(Math.PI/obj.n));
		System.out.println("The area is: " + area);
		return area;
	}
	public String toString() {
		//return String.format("%s%n%s","n= " + n, "length is " + length);
		return "RegularPolygon{" + "number of sides='" + this.n + '\'' + ',' + "length of sides= " + this.length + '}';
	}


	public static void main(String[] args) {
		//creating new polygon objects
		RegularPolygon pol1 = new RegularPolygon(3,10.0);
		RegularPolygon pol2 = new RegularPolygon(6, 7.5);
		RegularPolygon pol3 = new RegularPolygon(8, 3.5);
		RegularPolygon pol4 = new RegularPolygon(12, 4.0);
		//adding the new objects to an array
		RegularPolygon [] polygon = {pol1,pol2,pol3,pol4};
		
		//Created an array to hold the area of the objects
		double [] area= new double[4];
		double [] perimeter=new double[4];
		for (int i=0; i < polygon.length;i++) {
			System.out.println(polygon[i]);
			getArea(polygon[i]); // get the area for each new object
			getPerimeter(polygon[i]);// get the perimeter for each new oject
		}
		//this is where i tried to implement the max and min for the area 
		for (int j=0; j < area.length;j++) {
			area=new double[]{getArea(polygon[j])}; //tried to append the polygon area values to a new array
			perimeter=new double[] {getPerimeter(polygon[j])}; //tried to append the polygon perimeter values to a new array
			double max = area[0]; //set initial max value
			double min= perimeter[0];// set initial min value
			if (area[j]>max) { // if area at index j is greater than max 
					max=area[j]; //set max to that new higher value
				}
				System.out.println("max area " + max); // print max value
			if (area[j]<min) {//if area at index j is less than min 
				min=area[j];//set min to that new lower value
			}
			System.out.println("min perimeter " + min);//print the miimum value in the array
			}
        	
// i think the main issue is that the values are not being added to the array correctly as it only return the first value each time.			
			}
}




