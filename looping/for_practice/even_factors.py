# wap to print all the even factors of the given number

n = int(input("Enter a number: "))

for i in range(1,n+1):
    
    if n % i == 0 and i % 2 == 0:
            
            print(i)