#program that finds all the perfect numbers upto and including that number entered by user.
#prompt user for a positive integer.
#define a function
#initalise total
#for i in the range 1,number
#if num mod i is 0
#increment total i
#return when total is equal to num

#ask user for input
#for i in range 1 to number +1
#if total == num in loop 
#print i
def perfect(num):
    
    total=0
    for i in range(1,num):
        if num % i == 0:
            total+=i
    
    return total==num
    
number=int(input('Enter a positive integer:'))
for i in range (1,number+1):
    if perfect(i):
        print(i)
    
