def isPrime(n):
    
    #creating an empty list to hold all primes
    
    PrimeList=[]
    
    
    for i in range(2,n+1):
       PrimeList.append(i)
        
       if  i not  in PrimeList: 
        print(i)
        for j in range(i*i,n+1,i):
            PrimeList.append(j)
            
    return PrimeList
    
    #Driver code
       
n=100

isPrime(n)