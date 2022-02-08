#Program to print out the largest of two numbers entered by the user
# Uses two functions:  max and print_max
def print_max():
    """Function that prints out the largest of two numbers
    Uses the function max to find the largest"""
    def max(a, b):
        """Function that returns the largest of its two arguments"""
        if a > b:
            return a
        else:
            return b

        
        # Prompt the user for two numbers
    number1 = float(input('Enter a number:  '))
    number2 = float(input('Enter a number:  '))
    print('The largest of', number1, 'and', number2,'is', max(number1, number2))
    return
print_max()

#when we ask the program to print_max()
#it instructs the program to print the results of the function that is nested (max function) within the print_max function
#as the print_max function has no variable assigned and just empty parentheses.
