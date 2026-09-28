# print the odd number count from 1 to n

n = int(input("Enter a number: "))

count = 0
for i in range(1,n+1):
    
    if i % 2 != 0:
        
        count += 1
        
print(f"The total count of odd numbers from 1 to {n} = {count}")