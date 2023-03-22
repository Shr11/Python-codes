def isPrime(n):
    
    #creating an empty list to hold all primes
    
    PrimeList=[]
    
    #inserting no.s 2 to n
    i=2
    for i in range(2,n+1):
       PrimeList.append(i)
        
       for i  in PrimeList: 
        for j in range(i*i,n+1,i):
            PrimeList.remove(j)
            
    return PrimeList
    
    #Driver code
       
n=100

print(isPrime(n))