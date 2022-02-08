#Program to convert a string of digits into base 10
#should also be able to convert to hexadeciaml or base 16
#function with two arguments
#print int number, base

#ask user for string of numbers
#ask user for base to convert number to
#call the function.

def conversion(n,b):
    '''A function that takes two arguments a string of numbers and converts number into base 10 and a base.

        Will also convert for hexadecimal numbers if provided with base 16''' 
    print(int(n,b))
    

    

    
    
            
number=input('Enter a string of digits to convert:')
base=int(input('Enter the conversion base:'))

print(conversion(number,base))
