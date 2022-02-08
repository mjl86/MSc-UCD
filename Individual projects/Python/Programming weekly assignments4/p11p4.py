#initalise counters
#total1=1
#total2=1
#Ask user for input n1 (n1=int(input('Enter a number:'))
#Find the factorial of n squared using for and assign it n2
#n2=n1*2
#for i in range (1,n2):then
    #total1*=i
    #fact1=total1*n2


#Find n+1 and assign a new value n3
#n3=n1+1
#for i in range (1,n3):then
   # total2*=i
    #fact2=total2*n3
#catalan = equation (2n)!/(n+1)!*n!
#catalan=(fact1)/(fact2*n1)
#print('The number of Catalan numbers are',catalan)


total1=1
total2=1

n1=int(input('Enter a number:'))

n2=n1*2
for i in range (1,n2):
    total1*=i
    fact1=total1*n2

n3=n1+1
for i in range (1,n3):
    total2*=i
    fact2=total2*n3

catalan=(fact1)/(fact2*n1)
print('The numbers of Catalan numbers are',catalan)

