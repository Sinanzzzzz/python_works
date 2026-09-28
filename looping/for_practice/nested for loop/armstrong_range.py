# wap to get the armstrong numbers from a given range of 1 to 1000

for num in range(1,1001):
    
    temp = num
    sum = 0
    length=len(str(num))
    
    while(num > 0):
        digit = num % 10
        sum += digit ** length
        num //= 10
        
    if temp == sum:
        print(f"{temp} is armstrong number")