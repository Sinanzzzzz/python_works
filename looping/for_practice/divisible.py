# wap to print the numbers which are divisible by 3 and 5 from 1 to n

n = int(input("Enter a number: "))

for i in range(1,n+1):
    
    if i % 3 == 0 and i % 5 == 0:
        
        print(i)