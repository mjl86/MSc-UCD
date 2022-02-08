#Square root often can't find an exact solution
#initalise epsilon how much tolerance we will give to the approximation
#add variable that will move through the integers i.e step
#prompt user for int(input)
#if number>0
    #root=0
    #While abs(number-root squared) is >= epsilon and root <=number
        #root+=step
    #if abs(number-root**2)<epsilon
        #print(root is the approx square root
    #else:
        #if root is not evenly divisible (%2!=0)
            #print its notr a perfect square
    
#else
    #print(Program finishes when a negative number is entered.)

epsilon=.5
step=epsilon**2


number=int(input('Enter a number to find the square root of:'))
if number>0:
    root=0
    while abs(number-root**2)>=epsilon and root**2 <=number:
        root+=step
    if abs(number-root**2)<epsilon:
        print(root ,'is the approximate square root')
        
    else:
        if root %2!=0:
            print('It is not a perfect square')
else:
    print('program finished negative number entered')
