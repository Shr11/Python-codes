
#list comprehension

def lessThan(lst  ,  k):
    list = [ i for i in lst if i<k]
    return list
    
    
    
#utility code

l= list(map(int,input().split()))

k=int(input("Print less than _"))

print(lessThan(l, k))
