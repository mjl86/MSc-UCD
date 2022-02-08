#initalise counter for totals
#Ask manager for in put of toppings available int(input)
#int(input(the number of toppings on offer:))
#amount of toppings on a standard pizza
#int(input(the number of topping on a standard pizza))
#Find the factorial of each input by
#for n in range (1, toppings)
    #total*=n
    #fact=total2*toppings
#print the factotrial is fact
#do above step for both standard and available toppings swapping to appropriate variable
#initalise r (toppings-standard)
#repeat finding factorial swapping variable for r
#possible combinations equation is the going to be total1/(fact2*(the fact of toppings -standrard)
#Print(total number of combinations are combination.

total1=1
total2=1

n1=int(input('Enter a number:'))

n2=n1*2
for i in range (1,n2):
    total1*=i
    fact1=total1*n2
print('The factorial is',fact1)

n3=n1+1
for i in range (1,n3):
    total2*=i
    fact2=total2*n3
print('The factorial is',fact2)




catalan=(fact1)/(fact2*n1)
print('Catalan number are',catalan)
