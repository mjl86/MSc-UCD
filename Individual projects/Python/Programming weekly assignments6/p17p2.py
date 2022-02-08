#(a)
#function findDivisors (num1,num2)
#initalise divisors to include 1 
#for i in range (2,max( numb1 divided by 2, num2divided by 2)+1 do
#   if num1 mod i ==0 or num2 mod i == 0
#       add i to divisors
#return divisors.
#(b)
#ask user for input
#if the numbers entered are not positive then
#print out an error message
#else call function and assign to divisors
#print out the common divisors of number1 and number2 are divisors.




#(a)
def findDivisors(num1,num2):
    """finds the common divisors of num1 and num2

    assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    
    divisors = (1,)
    for i in range(2,max(num1//2,num2//2) +1):
        if num1 % i ==0 and num2 % i == 0:
            divisors +=(i,)
            
            
    return divisors
    
    

#(b)
number1=int(input('Enter a number:'))
number2=int(input('Enter a number:'))
if number1<=0 or number2<=0:
    print('Error only positive numbers allowed')
else:
    divisors = findDivisors(number1,number2)
    print('the common divisors of',number1,'and',number2, 'are',divisors)

    
