#initalise counter
#while x <=0
    #ask the user for int(input)
    #read number
    #while number(x) is in ranges
    #==0,0<x<20,20<x<40,40<x<60,60<x<80,80<x<100,100<x
        #while x == to a range count the number of x in each range
    #if x <0 print analysis a count of numbers in each range
    #x should not be <0 else program terminates


a,b,c,d,e,f,g=0,0,0,0,0,0,0
x=0
total=0
while x>=0:
    x=int(input('Enter a number(x) to see what range it is in:'))
    if x==0:
        print('x is equal to 0')
        a+=1
    elif x>0 and x<20:
        print('x is in range 0<x<20')
        b+=1
    elif x>20 and x<40:
        print('x is in range 20<x<40')
        c+=1
    elif x>40 and x<60:
        print('x is in range 40<x<60')
        d+=1
    elif x>60 and x<80:
        print('x is in range 60<x<80')
        e+=1
    elif x>80 and x<100:
        print('x is in range 80<x<100')
        f+=1
    elif x>100:
        print('x is in range x>100')
        g+=1
    x+=1
else:
    if x <0:
        print('Total numbers ==0:',a)
        print('Total numbers 0<x<20:',b)
        print('Total numbers 20<x<40:',c)
        print('Total numbers 40<x<60:',d)
        print('Total numbers 60<x<80:',e)
        print('Total numbers 80<x<100:',f)
        print('Total numbers x>100:',g)
        print('negative number entered the program has ended')
