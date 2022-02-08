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
total3=1
toppings=int(input('How many toppings are there today?'))
standard=int(input('How many toppings will be offered on a standard pizza?'))

for n in range (1,standard):
    total2*=n
    fact2=total2*standard
print('The factorial is',fact2)
for n in range (1,toppings):
    total1*=n
    fact1=total1*toppings
print('The factorial is',fact1)

r=toppings-standard
for n in range (1,r):
    total3*=n
    fact3=total3*r
print('The factorial is',fact3)

combination=fact1/(fact2*fact3)
print('Total combinations are',combination)



        
        
        


