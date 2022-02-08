#Program to calculate the Fibonacci Series
#initalise counter number=1
#While number >0: do
#   f_0, ,f_1=0,1
  #  number=int(input('enter what you want to calculate:'))
    #if number==1: then
      #  print('series is',f_0)
    #elif number<=0: then
       #print('program ended a negative number entered')
    #else:
        #print(Series is: f_0, f_1, sep = "", end = "")
        #i=2
        #for i in range(2, number):
            #f_0,f_1=f_1,f_0+f_1
            #print(',', f_1, end = "")
        #i += 1


number=1

while number>0:
    f_0,f_1=0,1
    number=int(input('enter what you want to calculate:'))
    if number==1:
        print('series is',f_0)
    elif number<=0:
        print('program ended a negative number entered')
    else:
        print('Series is:', f_0, ', ', f_1, sep = "", end = "")
        i=2
        for i in range(2, number):
            f_0,f_1=f_1,f_0+f_1
            print(',', f_1, end = "")
        i += 1
  

