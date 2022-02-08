#(a)Write a recursive function
#take argument as integer >=1
#if true return the number of terms from given series f(n-1)+2**n-1
#else
#result= 1
#return x

#(b)
#ask user for input
#while number >0
#call the function
#ask user for input
#else if a negative number entered return error message.
def series(x):
    """a function that has a single argument greater or equal to 1 and print out the terms of f(n-1)+2**n-1

    it assumes it is a non negative integer
    its recursive, the base case is 1"""
    if x >= 1:
        result = series(x-1) + 2**(x-1)
        print (result)
        return result
    else:
        result = 1
    return x
#(b)

number=int(input('enter a positive number:'))
while number >=1:
    series(number)
    number=int(input('enter a positive number:'))
else:
    if number<=0:
        print('a negative number was entered program ended')
    
