#(a)A function to find the approx square root
#it takes two arguments a number and a tolerance
#define the tolerance
#define the step
#initalise root as 0
#while the absolute (number-root squared)>=tolerance and root squared <=number: then
#increment root by step
#if the absolute (number- root squared < tolerance then
#return root
def square(x):
    epsilon=.5
    step=epsilon**2
    root=0
    while abs(number-root**2)>=epsilon and root**2 <=number:
        root+=step
    if abs(number-root**2)<epsilon:
        return root
        
    

#(b)
   # Ask user for a positive number of type float
   #if the number greater than 0 then
   #print def square(x)
   #else print an error a negative number has been entered
   #program ends
number=float(input('Enter a positive number to find the square root of:'))
if number >0:
    print(square(number))
else:
    print('program finished negative number entered')
