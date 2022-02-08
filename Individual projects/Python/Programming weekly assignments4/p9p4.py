#Define number
#while number>=0
    #i=1
    #fact=1
    #ask the user for a positive integer int(input(number?))
    #while i<= number
        #fact*=i
        #print( the factorial is fact)
        #i+=1
#else:
#   if number <0:
#       print(the program has ended a negative number has been entered)


number=0
while number>=0:
    i=1
    fact=1
    number=int(input('Enter the number you want the fatorial of:'))
    while i<=number:
        fact*=i
        print('The factorial is ', fact)
        i+=1
else:
    if number<0:
         print('the program has ended a negative number has been entered.')
    
