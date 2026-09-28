# Define a function that takes string as argument and print the count of
# digits, spaces, letters in that string

def string(s):
    digit = 0
    space = 0
    letter = 0
    
    for i in s:
        if i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1
        else:
            letter += 1
            
    print("Digits:",digit)
    print("Spaces:",space)
    print("Letters:",letter)
    
string("hello world")