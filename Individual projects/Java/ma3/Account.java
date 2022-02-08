package ma3;

import java.util.Date;
// program to create an account and display the date created and perform withdrawals and deposits
public class Account {
	private int id=0;
	private double balance=0;
	private Date dateCreated=new Date();
	private double annualInterestRate;	
// no arg constructor	
	public Account() {
	
	}
//constructor that creates and account with a specified id balance and datecreated	
	public Account(int i, double b, Date d) {
		this.id=i;
		this.balance=b;
		this.dateCreated= d;
		
		
	}
	
// Getters
//getter for the variable id	
	  public int getId() {
	    return this.id;
	  }
//getter for the variable balance	  
	  public double getBalance() {
		  return this.balance;
	  }
//getter for the variable annual interest rate	  
	  public double getAnnualInterestRate() {
		  return annualInterestRate;
	  }
// getter for the variable date created
	  public Date getDateCreated() {
		  return dateCreated;
	  }

// Setters
//Setter for the variable id
	  public int setId(int newId) {
	    return this.id = newId;
	  }
//Setter for the variable balance
	  public double setBalance(double newBalance) {
		 return this.balance=newBalance;
	  }
//Setter annual interest rate
	  public double setAnnualInterestRate(double newAnnualInterestRate) {
		  return this.annualInterestRate=newAnnualInterestRate;
	  }
	  
	  
//a method to calculate the monthly interest amount
	  public static double getMonthlyInterest(Account obj) {
		  Account rate=new Account();
		  double monthlyInterestAmount=obj.balance*(rate.setAnnualInterestRate(4.5/100)/12);
		  System.out.println("The monthly interest amount is " + monthlyInterestAmount);
		  return monthlyInterestAmount;
	  }
	  
// A method to calculate a withdrawal on the account	  
	  public static void withdraw(Account obj,double debit) {
		  double x=obj.balance;//setting a variable to the account balance
		  System.out.println("Current balance is " + x);
		  double updatedBalance=x-debit; //calculating the updated balance after withdrawal
		  obj.setBalance(updatedBalance);//setting the new account balance
		  System.out.println("New balance after withdrawal " + updatedBalance);//printing the updated balance
	  }
	  
// A method to calculate a deposit on the account	  
	  public static void deposit(Account obj,double credit) {
		  double x=obj.balance; //setting a variable to the account balance
		  System.out.println("Current balance is " + x);
		  double updatedBalance=x+credit;//calculating the updated balance after deposit
		  obj.setBalance(updatedBalance);//setting the new balance
		  System.out.println("New balance after deposit " + updatedBalance);//printing the new balance
		
	  }
// A toString method	  
	public String toString() {
	      return String.format("%s%n%s%n%s", "Account number: " + id, "Account balance: " + balance, "Date created: " + dateCreated);
	      
	   }
	
//Main test program	
	public static void main(String[] args) {
		Account date=new Account();
		Date d=date.getDateCreated();// assigns the date to account
		Account obj=new Account(101,20000.00,d); // creating a new account object with specified arguments
		withdraw(obj,2500.00);//calling the withdrawal method
		deposit(obj,3000.00);// calling the deposit method
		getMonthlyInterest(obj);// getting the monthly interest on the account on the new balance after withdrawal and deposit
		
		System.out.println("Account created " + d);
		
		
		}
}
