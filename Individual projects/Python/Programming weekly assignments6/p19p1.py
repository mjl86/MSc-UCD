#division number by base
#while number >0
#get remainder of division n % b
#divide number by supplied base until 0
#print the remainder to get number represented in the new base.
def conversion(n,b):
    '''A function that takes a number in base 10 and another base and converts number into a number in the base supplied.''' 
    while n > 0:
        r= n%b
        n=n//b
        print(r)
    

    

    
    
            
        


number=int(input('Enter a base 10 number:'))
base=int(input('Enter the conversion base:'))

print(conversion(number,base))
