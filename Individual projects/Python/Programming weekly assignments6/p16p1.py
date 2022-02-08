#(a)
#define a recursive function. it should take a single argument >=1 and print out the number of terms from
#equation f(n)=2*f(n-1)
#if x>=1
#assign equation to variable
#print the result of equation
#increment by base case
#return the result
#else return 1
#(b)
#Prompt the user for an integer
#check that the number >=1
#while true
#   call function
#   ask user for input
#else:
#   print(error only positive integers >=1 allowed)

def series(x):
    if x>=1:
        form= 2*series(x-1)
        print (form)
        form*=2
        return form
    else:
        return 1

number=int(input('enter a positive number:'))
while number >=1:
    series(number)
    number=int(input('enter a positive number:'))
else:
    print('error only positive integers >=1 allowed')
    

        
