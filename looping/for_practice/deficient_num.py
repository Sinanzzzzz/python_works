# deficient number

# wap to check the given number is deficient or not

n = int(input("Enter a number: "))

sum = 0

for i in range(1,n):
    
    if n % i == 0:
        
        sum += i
        
if sum < n:
    print("Deficient number")
else:
    print("Not Deficient number")