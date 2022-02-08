#program to print out the largest of two numbers entered by the user
# Uses a function max
# Uses max in a print statement
def max(a, b):
    """Function that returns the largest of its two arguments"""
    if a > b:
        return a
    else:return b

    
# Prompt the user for two numbers
number1 = float(input('Enter a number:  '))
number2 = float(input('Enter a number:  '))
print('The largest of', number1, 'and', number2, 'is',max(number1, number2))
print('Finished!')


#If the previous example we assigned the function to a variable biggest.
#in this example we used the function directly in the program with our values of number1 and number2 taking the place of a and b
