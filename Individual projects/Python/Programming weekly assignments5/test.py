class myDateJ:
    __dayArr= ['Saturday','Sunday','Monday','Tuesday',
          'Wednesday','Thursday','Friday']
    def weekday(self): 
        i = (self.__jDay + 3) % 7
        return myDateJ.__dayArr[i]

print(myDateJ)
