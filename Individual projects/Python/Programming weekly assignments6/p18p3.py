#A function to return the number of times the string "code" case sensitive appears.
#function
#create a list with all variable of code
#initialise counter
#iterate through list using for
#if i in string
#increment total by 1
#return the total count
def case(str):
    '''A function to count hpow many times code appears in a given string.

        assumes that str is a string and that index position [2] or d is interchangable with other letters and is not case sensitive.'''
    
    list=['code','coae','cobe','coce','coee','cofe','coge','cohe','coie','coje','coke','cole','come','cone','cooe','cope','coqe',
          'core','core','cote','coue','cove','cowe','coxe','coye','coze',
          'coAe','coBe','coCe','coDe','coEe','coFe','coGe','coHe','coIe','coJe','coKe','coLe','coMe','coNe','coOe','coPe','coQe',
          'coRe','coSe','coTe','coUe','coVe','coWe','coXe','coYe','coZe',]
    total=0
    for i in list:
        if i in string:
            total+=1
    return total
    


#test program to make sure it worked.
string=input('Enter a string:')
print(case(string))
