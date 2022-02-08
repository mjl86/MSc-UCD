#program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
#Find all the pairs of factors that multiply for that number
# for a number in specified range 2 upto 20 do
#   for i in a range of 2-number do
#       while number is evenly divisble by i then
#           print (number equals i * number divided by i)
#           break loop
#   else:
#       print the number is a prime number.


for number in range(2, 20):
    for i in range(2, number):
        while number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
        print(number, 'is a prime number')
print('Finished!')


