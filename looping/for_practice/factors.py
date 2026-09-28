# wap to get the factors of the number given

n = int(input("Enter a number: "))

for i in range(1,n+1):
    
    if n % i == 0:
        
        print(i)