#(a)
#function findDivisors (num1)
#initalise divisors to include 1 and the number
#for i in range 2, number divided by 2 +1) do
#   if num1 mod i ==0 
#       add i to divisors
#return divisors.
#(b)
#ask user for input
#if the numbers entered are not positive then
#print out an error message
#else find the divisors
#print out the divisors




#(a)
def findDivisors(num1):
    """finds the common divisors of num1 and num2

    assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    
    divisors = (1,num1)
    for i in range(2,num1//2+1):
        if num1 % i ==0:
            divisors +=(i,)
            
    return divisors
        
    

#(b)
number1=int(input('Enter a number:'))

if number1<=0:
    print('Error only positive numbers allowed')
else:
    divisors = findDivisors(number1)
    print('the divisors of',number1,'are',divisors)

    
