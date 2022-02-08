#program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# Look for prime numbers in a range of integers
for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
    # loop fell through without finding a factor
        print(number, 'is a prime number')
print('Finished!')


#The range is between 2 and 20 so it'll only calculate to 19 we would need to add 20+1 to range if we wanted to include 20.
#if number is evenly divisible by a number in that range print the number and what numbers multiple to make it e.g 4=2*2 or 9=3*3
#if above is false the loop breaks and moves onto the else statement otherwise the first loop will repeat until the number is not evenly divisible.

