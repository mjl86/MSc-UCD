#initalise a count and a total variable.
#User int(input(positive number))
#if number > 0 do
    #Addition of all integers upto and including number.
    #While count >=0 and <= number
    #total+=count
    #print(total of count is count)
    #count+=1

total =0  
count=0
number=int(input('Enter a positive number: '))
if number>0:
    while count >= 0 and count<=number:
        total+= count
        print('the total is',total)
        count+=1
        
        
