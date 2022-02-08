#Program to calculate the Fibonacci Series
#(a)
#Write a function calculate the Fibonacci number
#it assumes that it argument is a positive integer.
#initalise variables
#f_0, ,f_1=0,1
  #if x<=1: then
      #  Return a value of 0
    #else:
       #return (fibonacci-1)  +  (fibonacci-2)
#(b)
    #program to get the fibonnaci number from a positive integer.
#  number=int(input('enter what you want to calculate:'))
#if number<=0: then
       #print('negative number program ended')
#else:
    #for i in range (number):do
       # print(fibonacci(i))

#(a) define function

def fibonacci(x):
    if x<=1:
        return x
    else:
       return(fibonacci(x-1)+ fibonacci(x-2))
    
#(b)

number=int(input('enter a positive number:'))
if number<=0:
        print('a negative number was entered program ended')
else:
    for i in range (number):
        print(fibonacci(i))
