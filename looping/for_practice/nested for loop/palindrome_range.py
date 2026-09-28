# wap to get the palindrome numbers from a given range of 1 to 1000

for number in range(1,1001):
    
    temp = number
    reverse = 0 
    
    while(number>0):
        digit = number % 10
        reverse = reverse * 10 + digit              
        number = number // 10                      
        
    if temp == reverse:
        print(f"{temp} is Palindrome")
        
        