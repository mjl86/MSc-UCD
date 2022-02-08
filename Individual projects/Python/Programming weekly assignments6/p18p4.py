#a function that has two arguments and return true if either string appears at the very end of the other string.
#function to change uppercase letters to lower case.
#initalise variable a to a.lower
#create empty string
#iterate using for i in a
#if a lower case letter
#add it to the empty string
#repeat for 2nd variable b
#inialise function to see if string a ends with string b or if stringb ends with string a
#if a then b or if b then a
#return true

def atend(a,b):
    
            '''Tests if string a ends with string b or string b ends with string a

                it is not case sensitive assumes arguments are strings'''
    def tochars(a,b):
        '''Coverts strings to lowercase letters'''
        a=a.lower()
        astring=''
    
        for i in a:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                astring+=i
        return astring
     
        b=b.lower()
        bstring=''   
        for y in b:
            if y in 'abcdefghijklmnopqrstuvwxyz':
                bstring+=i
        return bstring
      
    def match(a,b):
        '''Checks if one string ends with the other'''
        if a.endswith(b) or b.endswith (a):
           return True
    return match(tochars(a,b),tochars(b,a))



#test program to make sure it worked.
a_string=input('Enter a string:')
b_string=input('Enter a string:')
print(atend(a_string,b_string))




