# wap to get the sum of odd factors of the number given

n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    
    if n % i == 0 and i % 2 != 0:
            
            sum += i
            
print(f"The sum of odd factors of {n} = {sum}")