#Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Exits when an empty string is entered
def isPalindrome(s):
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
        for c in s:
        # ...  and add the character to the string if it is a letter
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring


    def isPal(s):
        """Checks whether the string s is a palindrome

        Assumes that s is a str with only lowercase letters and no
        non-letters.
        Returns True if s is a palindrome;
        Returns False otherwise.
        Recursive function."""
        if len(s) <= 1:
# A palindrome of length 0 or 1 is a palindrome
            return True
        else:
# Compare the first and the last letters and check the remainder
#       of the string
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
str = input('Enter a string (empty string to exit):  ')
while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input('Enter a string (empty string to exit):  ')
print('Finished!')
