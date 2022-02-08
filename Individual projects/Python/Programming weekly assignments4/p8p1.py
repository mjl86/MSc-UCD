#A program that prompts for an input of a series of numbers.
#While the number is >0
#int(input(please enter a series of numbers))
#Test if number enter >0
#Checks wheather each number is divisible by 2,3,5,7
#If num % 2,3,5,7==0
#print(which number it is divisble by)
#Program continues until a negative number is entered
#program terminates

num=0
while num>=0:
    num=float(input('please enter a number:'))
    if num>0 %2==0:
        print(num,'is divisible by 2')
    if num>0 %3==0:
        print(num,'is divisible by 3')
    if num>0 %5==0:
        print(num,'is divisible by 5')
    if num>0 %7==0:
        print(num,'is divisible by 7')
else:
    if num<0:
        print('that is a negative number the program is finished')
