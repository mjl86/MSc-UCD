#A program that tests if a file exists and if not prints it doesn't exist
#Else: it opens it to read
#and counts the () [] {} <> bracket pairs
#close file
#and print results of all counters
#if right bracket equals number of left bracket type
#print brackets are balanced
#else#print brackets are not balanced.



import os
filename='sourcecode.txt'
if not os.path.isfile(filename):
    print('File ' + filename + ' does not exist.')
else:
    file=open(filename, 'r')
    data=file.read()
    totala=data.count('<')
    totalb=data.count('>')
    totalc=data.count('(')
    totald=data.count(')')
    totale=data.count('{')
    totalf=data.count('}')
    totalg=data.count('[')
    totalh=data.count(']')
    file.close()
    

    print ('number of <:',totala)
    print ('number of >:',totalb)
    print ('number of (:',totalc)
    print ('number of ):',totald)
    print ('number of {:',totale)
    print ('number of }:',totalf)
    print ('number of [:',totalg)
    print ('number of ]:',totalh)

if totala==totalb and totalc==totald and totale==totalf and totalg==totalh:
    print("All the brackets are balanced")
else:
    print("the brackets are not balanced")
    

