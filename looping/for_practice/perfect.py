# perfect number

# wap to check the given number is perfect or not

n = int(input("Enter a number: "))

sum = 0

for i in range(1,n):
    
    if n % i == 0:
        
        sum += i
        
if sum == n:
    print("Perfect")
else:
    print("Not perfect")