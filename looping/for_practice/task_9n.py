# Print all numbers that have exactly 4 factors.

for num in range(1,100):
    
    count = 0
    
    for i in range(1,num+1):
        
        if num % i == 0:
            count += 1
    if count == 4:
        print(num)