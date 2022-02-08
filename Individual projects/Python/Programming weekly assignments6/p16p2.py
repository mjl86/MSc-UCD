#(a)
#function findDivisors (num1,num2)
#initalise divisors
#for i from 1 to min(num1,num2) do
#   if num mod i ==0 and num2 mod i==0 then
#       add i to divisors
#return divisors.
#(b)
#if the numbers entered are not positive then
#print out an error message
#else find the common divisors
#print out the common divisors
#sum the common divisors
#print out the total



#(a)
def findDivisors(num1,num2):
    """finds the common divisors of num1 and num2

    assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    
    divisors = ()
    for i in range(1,min(num1,num2) + 1):
        if num1 % i ==0 and num2 % i ==0:
            divisors +=(i,)
            
    return divisors
        
    

#(b)
number1=int(input('Enter a number:'))
number2=int(input('Enter a number:'))
if number1<=0 or number2 <=0:
    print('Error only positive numbers allowed')
else:
    divisors = findDivisors(number1,number2)
    print('the common divisors of',number1,'and',number2,'are',divisors)

    total=0
    for d in divisors:
        total+=d
    print('Sum of the common divisors is:',total)
        
            
