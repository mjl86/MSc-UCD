 #Program to illustrate scoping in Python
def f(x):
     """Function that adds 1 to its argument and prints it out"""
     print('In function f:')
     x += 1
     y = 1
     print('x is', x)
     print('y is', y)
     print('z is', z)
     return x


x, y, z = 5, 10, 15
print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)



z = f(x)
print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)

#Scoping the program looks for the closest variable to itself.
#in the before function f x y z have been assigned variables so the program uses them.

#in the function f(x)
#x has been incremented by one so it take the x from before function and adds one.
#y has been assigned a value so thats taken as y value.
#the closest z value is in the before function program so it uses that as z value as there was no assignment made in f(x).

#After f(x)
#x is the value of x in before function as its the closest variable x.
#y is the value of x in before function as its the closest variable y.
#z has been given a new value of f(x) and in function f x=6.
