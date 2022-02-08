 #Program to illustrate scoping in Python
def f(x):
     """Function that adds 1 to its argument and prints it out"""
     print('In function f:')
     x -= 1 #x now is four as i'm subtracting one.
     y = 1# tried to do a plus or minus increment but was unable as y a local variable has not been refernced yet 
     z=5 #introduced a variable for z so in function of z now=5
     print('x is', x)
     print('y is', y)
     print('z is', z)
     return y # changed to y now z in after function = 1 and not 6 like in original program


x, y, z = 5, 10, 15
print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)



z = y #if i remove the f(x) from here the function is completely left out as its not called and only before and after function have output.l
print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
