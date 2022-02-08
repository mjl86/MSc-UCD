#Prompt the user for a number.#int(input(give me a number))
#initalise counters
#x=1 y=2 as we want to start from one (and if y is initalised at 1 also we get two number ones at  the start of our table
    #while x<table_size (the number user enters)
        #print(x) suppress new line function by using end= and tab across to give table shape using \t
            #while y is less than table_size print(x*y end=\t)
#increment each variable by 1
  #          (y+=1)
   #     (x+=1)



table_size=int(input('Enter the number you want a multplication table for:'))
x=1
while x<=table_size:
    y=2
    print('\n')
    print(x,end='\t')
    while y <= table_size:
        print(x*y,end='\t')
        y+=1
    x+=1
    

   
