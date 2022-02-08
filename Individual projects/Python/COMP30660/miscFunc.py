import math
import time
import multiprocessing
from multiprocessing import Pool

def my_func(x):
    s=math.sqrt(x)
    return s


def my_func_verbose(x):
    s=math.sqrt(x)
    print ("Task",multiprocessing.current_process(),x,s)
    return s

def check_prime(num):
    t1=time.time()
    res = False
    if num > 0:
        for i in range(2,num):
            if (num % i)==0:
                print(num, "is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:",int(time.time()-t1))
                break
        else:
            print(num,"is a prime number")
            print("Time:",time.time()-t1)
            res=True
    return res

def fact(x):
    total=1
    t1=time.time()
    for i in range (1,x+1):
        total*=i
    print("Time:",int(time.time()-t1))
    return total
