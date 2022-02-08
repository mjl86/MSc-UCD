#A function to return the number of times the string "code" case sensitive appears.
#function
#Return x.count string "code"
def case(x):
   """Counts how many times the string "code" appears in a given string

        Assumes that x is a str and is case sensitive"""
   return x.count('code')



#test program to make sure it worked.
string=input('Enter a string:')
print(case(string))
