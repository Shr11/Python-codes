
#function definition

def fun( z , a, x= 20, y=10 ):                    # x,y are default arguments & z,a are keyword arguments
    sum = x + y                                   # default sum = 30
    product = a*z
    return f'sum is {sum} & product is {product}' #using f string instead of "{} {}".format(sum,product)
   
   
#function call   
    
string = fun(z = 10,a=50)                         #But default arg always follows non default arguments in parameters
print(string)

