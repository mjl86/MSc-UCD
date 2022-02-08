#Calculating the factorial of a number
# Program prompts the user for the number
#if number<0
    #print an error message.
#else:
    #if number >=0:then
        #fact=1 &
        #i=1
#   while i<=number:do
        #fact*=i
#       i+=1
#   Print the factorial of number is fact.


number = int(input('Enter the number for which you wish to calculate the factorial:'))
if number < 0:
    print('Error:  Number entered was less than 0.')
else:
    if number >=0:
        fact=1
        i=1
    while i <=number:
        fact*= i
        i+=1
    print('Factorial of', number, 'is', fact)
    print('Finished!')
