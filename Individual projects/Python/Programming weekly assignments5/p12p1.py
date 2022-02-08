#Programme to find the factorial of a positive number
#(a)
#Define a function that returns the factorial of its argument.
#That assumes the argument is non-negative.
#initialise total=1
#use for loop to calculate the factorial of users input.
#for i in range (1,number+1)
#Multiply total by 1 across the range and
#return total
    
    
#(b)

#ask the user for a positive integer int(input(number?))
#if number is >=0:
#print(the factorial of number is fact*number)
#else:
    #print('Error number must be positive.')


#(a)
def fact(x):
    total=1
    for i in range (1,number+1):
        total*=i
    return total
 #(b)   
number=int(input('Enter a positive number you want the fatorial of:'))    
if number>=0:
    print('The factorial of',number,'is',fact(number))
else:
    print('Error number must be positive.')

    
