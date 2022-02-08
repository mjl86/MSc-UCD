#While count >=0 do:
    #intialise total
    #User int(input(positive number))
    #Addition of all integers upto and including number.
    #for count in range (0,number+1) want to include number
    #total+=count
    #print(total of count is total)
#else
    #print a negative number enter end program.


number=0
while number>=0:
    total =0
    number=int(input('Enter a positive number: '))
    for count in range(0,number+1):
        total+=count
        print('the total is',total)
        
else:
    if number<0:
        print('the program has ended a negative number has been entered.')
