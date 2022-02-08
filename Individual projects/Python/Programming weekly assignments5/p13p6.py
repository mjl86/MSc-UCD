def fact(x):
    """Function that calculates the factorial of a number it assumes that the argument is a non negative integer 
    x*fact(x-1) is showing us that a factorial is x multiplied by the factorial of the next smallest number fact(x-1)
        x is then replaced in our program by number so any input of type int can have its factorial calculated."""
    if x==0:
        return 1
    else:
        return x * fact(x-1)
#prompt the user for a number
number=int(input('Enter a positive number to get the factorial:'))
if number>=0:
    print(fact(number))
    
else:
    print('Error: Only positive numbers can be assesed:')

