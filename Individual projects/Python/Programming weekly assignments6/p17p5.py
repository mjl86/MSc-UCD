#Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Compare the first and the last letters and check the remainder of the string
# A palindrome of length 0 or 1 is a palindrome
# Exits when an empty string is entered
#The addition of print statements allow us to follow the loops as the program compares letters.
#for instance the word abba the isPal function loops three times to a base case of 0 and then it retruns the value as true.
#it loops through this also three times making sure each comparison is true.
#in a word that is not a palindrome the print statement returns false from isPal argument.
def isPalindrome(s):
    print ('the main function where there are two other functions nested')
    """Checks whether the string s is a palindrome
        Assumes s is a str.
        Returns True if the letters in s form a palindrome;
        Returns False otherwise.
        Case and non-letters are ignored."""
    def toChars(s):
        """Converts a string to lowercase and removes non-letters
            Assumes s is a str.
            Converts uppercase letters to lowercase and removes non-letters."""
    # First of all, convert uppercase letters to lowercase
        s = s.lower()
    # Start with an empty string
        letterstring = ''
    # Go through s...
        print('How the character is added to the empty string if it is a letter')
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
                print(letterstring)
        return letterstring


    def isPal(s):
        """Checks whether the string s is a palindrome

        Assumes that s is a str with only lowercase letters and no
        non-letters.
        Returns True if s is a palindrome;
        Returns False otherwise.
        Recursive function.
        Has print statements to trace its operation."""
        print ('isPal function called with argument',s)
        if len(s) <= 1:

            print('About to return True from isPal from the base case')
            return True
        else:

            result= s[0] == s[-1] and isPal(s[1:-1])
            print('About to return result',result,'from isPal argument',s)
            return result
    return isPal(toChars(s))


str = input('Enter a string (empty string to exit):  ')
while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input('Enter a string (empty string to exit):  ')
print('Finished!')
