#recursive fibonacci

def fib(n):
    if (n==1) or (n==0):
        return n
        
        
    elif n<0 :
        print("Enter valid number")
        return n
        
        
    else:
        return fib(n-1) + fib(n-2)


#iterative fibonacci

def fib_iter(n):
    a=0
    b=1
    if n==0:
        return 0
        
    elif n<0:
        print("Incorrect entry!") 
        return -1  
        
    elif n==1:
        return b
        
    else:
      for i in range(1,n):
        y=a+b
        a=b
        b=y
      return b
        
n = int(input())        

if n==-1:
  pass
else:  
  input("fibonacci of ", n ,"is ", fib(n))  

input(("fibonacci of",n,"is ", fib_iter(n)))

 