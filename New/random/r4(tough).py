# Define a function that takes a string as argument and returns a new dictionary
# where keys are characters and values are count of each character

def string(s):
    new ={}
    for i in s:
        new[i]=new.get(i,0)+1
    return new
    
print(string("hello world"))