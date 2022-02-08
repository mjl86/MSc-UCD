#Program to calculate the Fibonacci Series
#(a)
#Write a recursive function to calculate the Fibonacci number
#it assumes that it argument is a positive integer.
#function to calculate fibonacci series
  #if x<=1: then
      #  Return a value of 0
    #else:
       #return (fibonacci(x-1)  +  (fibonacci(x-2)
#(b)
    #program to get the fibonnaci number from a positive integer.
#  ask user for input
#while number > 0 do
    #for i in range (number):do
       # print(fibonacci(i))
       #ask user for input
#else:
    #if number<=0: then
       #print('negative number program ended')

    

#(a) define function

def fibonacci(x):
    """Function that returns the Fibonacci Series of its argument

    assumes that the argument is a non negative integer
    uses a recursive definition"""
    
    if x<=1:
        return x
    else:
       return(fibonacci(x-1)+ fibonacci(x-2))
    
#(b)

number=int(input('enter a positive number:'))
while number >0:
    for i in range (number):
        print(fibonacci(i))
        number=int(input('enter a positive number:'))
  
else:
    if number<=0:
        print('a negative number was entered program ended')

    
