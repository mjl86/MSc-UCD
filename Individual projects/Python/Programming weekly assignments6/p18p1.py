#Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Exits when an empty string is entered
def isPal(s):
        """Checks whether the string s is a palindrome

        Assumes that s is a str with only lowercase letters and no
        non-letters.
        Returns True if s is a palindrome;
        Returns False otherwise."""
        s=s.lower()
        letterstring=''
        for c in s:
        # ...  and add the character to the string if it is a letter
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        for i in range(0,int(len(s)//2)):
            if s[i] != s[len(s)-i-1]:
                return False
            else:
                 if len (s) <=1:
                    return true
# A palindrome of length 0 or 1 is a palindrome
        return True 
       
# Compare the first and the last letters and check the remainder of the string
       
            

str = input('Enter a string (empty string to exit):  ')
while str != '':
    if isPal(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input('Enter a string (empty string to exit):  ')
print('Finished!')




