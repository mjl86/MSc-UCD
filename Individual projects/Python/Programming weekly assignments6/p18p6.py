#A program that tests if a file exists and if not prints it doesn't exist
#Else: it opens it to read
#and counts the <,> ,/n , <!--, -->, e in the file
#create a results file to write to.
#if file already exists print file already exists
#else create new file called results.txt
#and print results of count to



import os
filename='sourcecode.txt'
if not os.path.isfile(filename):
    print('File ' + filename + ' does not exist.')
else:
    file=open(filename, 'r')
    data=file.read()
    totala=data.count('<')
    totalb=data.count('>')
    totalc=data.count('/n')
    totald=data.count('<!--')
    totale=data.count('-->')
    totalf=data.count('e')
    file.close()
    
newfile='results.txt'
if not os.path.isfile(newfile):
    print('file ' + newfile + ' already exists.')
else:
    resultfile=open(newfile, 'w')
    print ('number of <:',totala, file=resultfile)
    print ('number of >:',totalb, file=resultfile)
    print ('number of /n:',totalc,file=resultfile)
    print ('number of <!--:',totald,file=resultfile)
    print ('number of -->:',totale, file=resultfile)
    print ('number of e:',totalf,file=resultfile)
    
    resultfile.close()
newfile=open('results.txt','r')
print(newfile.read())
