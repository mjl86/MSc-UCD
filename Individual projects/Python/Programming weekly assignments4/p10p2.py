# Finding the integer cube root of a number
# If the number entered is negative, look for the cube root of its negation
#assign number a value
#while number does not equal 0
    # Program prompts the user for a number=int(input(enter a number))
    #if number== 0 program finishes
    #else:
        #if number<0:
            #change positive to negative new_number=-number
        #else:
            #new_number = number
        #assign variable cube_root = 0
        #while cube_root**3 <new_number:
            #cube_root += 1
        #if cube_root**3 == new_number:
            #if number<0:
                #change positive to negative cube_root=-cube_root
            #print('Cube root of', number, 'is', cube_root)
        #else:
                #print(number,'is not a perfect cube')


    
 

number=1
while number!=0:
    number = int(input('Enter the number for which you wish to calculate the cube root:'))
    if number==0:
        print('the program is finished')
    else:
        if number < 0:
            new_number = -number
        else:
            new_number = number
        cube_root = 0
        while cube_root**3 <new_number:
            cube_root += 1
        if cube_root**3 == new_number:
            if number<0:
                cube_root=-cube_root
            print('Cube root of', number, 'is', cube_root)
        else:
                print(number,'is not a perfect cube')



        


