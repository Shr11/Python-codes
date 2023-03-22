#importing math module

import math

#to check if a no is perfect square

def isPerfectSq(x):

    s= int(math.sqrt(x))
    
    return s*s==x
    
#to check if fibo
    
def isFib(n):

    #short ckt evaluation
    return isPerfectSq(5*n*n + 4) or isPerfectSq(5*n*n - 4)
    
    
#utility code

for i in range(int(input())):
    
    if isFib(i) == True:

        print(i)
