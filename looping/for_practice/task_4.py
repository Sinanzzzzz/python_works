# print the sum of odd  numbers from 1 to n

n = int(input("Enter a number: "))

sum = 0
for i in range(1,n+1):
    
    if i % 2 != 0:
        
        sum += i
        
print(f"The sum of odd  numbers from 1 to {n} = {sum}")