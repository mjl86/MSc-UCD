#(a)Write a recursive function
#take argument as integer >=0
#if true return the number of terms from given series f(n-2)+13*f(n-1)
#else
#return 1
#(b)
#ask user for input
#while number >=0
#call the function
#ask user for input
#else if a negative number entered return error message.
def series(x):
    """a function that has a single argument greater or equal to 0 and print out the terms of f(n-2)+13*f(n-1)

    it assumes it is a non negative integer
    its recursive, the base cases are 13 and 8"""
    if x >= 0:
        result = series(x-2) + 13*series(x-1)
        print (result)
        return result
    else:
        return 1
    
    
#(b)

number=int(input('enter a positive number:'))
while number >= 0:
    series(number)
    number=int(input('enter a positive number:'))
else:
    if number<0:
        print('a negative number was entered program ended')
    

#If you could provide some feedback as i couldn't get this program to work correctly i couldn't figure out how to address to base cases
        #after trying several variations.
