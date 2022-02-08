#A for loop to find the factorial n! of a positive integer.
#initialise total=1
#ask the user for a positive integer int(input(number?))
#read number
#use for loop to calculate the factorial of users input.
#for n in range (1,number)
    #total= n * total
    #factorial = total*number
#print(the factorial is fact)

total=1
number=int(input('Enter the number you want the fatorial of:'))
for n in range (1,number):
    total*=n
    fact=total*number
print('The factorial is',fact)
    
    
