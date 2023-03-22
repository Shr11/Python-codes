#lists to pair
l1 = list(map(int,input())) 

l2 = list(map(int,input()))

#resulted list by list comprehension

l3=[[l1[i],l2[i]] for i in range(len(l2))]

#result
print(l3)        
