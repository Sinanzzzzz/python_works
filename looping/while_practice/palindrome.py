# wap to reverse the number entered by user

number = 153

reverse = 0

while(number>0):
    digit = number % 10
    reverse = reverse * 10 + digit             # Important equation(cause reversed aaya 
    number = number // 10                      # numbers digit il aakaam)
    
print(reverse)