def evenWords(s):
    
    s=s.split(' ')
    
    for word in s:
        
        if len(word)%2==0:
            
            print(word)
string= "I am shraddha."
evenWords(string)
