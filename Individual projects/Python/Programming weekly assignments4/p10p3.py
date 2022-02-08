#a program to count the vowels a,e,i,o,u in a string
#initalise a counter
#assign the sting aeiou to variable vowels
#ask the user for a string input(string)
#for s in string
#   if s in variable vowels
#   increment the counter by number of vowels and
#       print out total vowels
#else if empty string entered print program finished.

vowels='aeiou'
count=0

string=input('enter a string:')
if string!=(''):
    for s in string:
        if s in vowels:
            count+=1
    print('total vowels in string are ',count)
else:
    print('nothing entered program has finished')
    
