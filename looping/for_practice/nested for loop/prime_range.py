# wap to get the prime numbers from a given range of 2 to 1000

for num in range(2,1001):
    
    for i in range(2,num):
        if num % i == 0:
            break
            
    else:
        print("Prime number",num)