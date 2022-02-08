#A function
#replace '.xyz' with another letter
#then test if xyz in string
#it it is return true
#else return false.

def noperiod(a):
    '''A function with one argument to to test if a string contains xyz not directly preceeded by a "."'''
    n=a.replace('.xyz','B')
    if 'xyz' in n:
        return True
    else:
        return False
        
    









#test program to make sure it worked.
string=input('Enter a string:')
print(noperiod(string))
