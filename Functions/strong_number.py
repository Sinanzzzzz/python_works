
def is_strong(num):
    
    temp = num
    sum = 0
    
    while(num > 0):
        
        digit = num % 10
        fact = 1
        
        for i in range(1,digit+1):
            
            fact *= i
        sum += fact
        num //= 10
        
    print(f"{temp} is a strong number" if temp == sum else f"{temp} is not a strong number")
    
is_strong(145)