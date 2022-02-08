#Program to calculate the Fibonacci Series
#assign variables f_0 and f_1 (0,1)
#ask the user for the number they wish to calculate
#if number==1:
#   print the series is f_0
#else
#   print the fibonacci series if f_0, f_1 seperate by a space end with space
#   a,b=f_0,f_1
#   i=2
#while i in range (2 to number) do
#   a,b=b,a+b
#print ,b end ''
#   increment i by 1

f_0,f_1=0,1

number=int(input('enter what you want to calculate:'))

if number==1:
    print('the Fibonacci series is',f_0)
elif number<=0:
    print('number entered was <=0')
else:
    print('The Fibonacci Series is:', f_0, ', ', f_1, sep = "", end = "")
    i = 2
    while i in range(2, number):
        f_0,f_1=f_1,f_0+f_1
        print(',', f_1, end = "")
        i += 1
