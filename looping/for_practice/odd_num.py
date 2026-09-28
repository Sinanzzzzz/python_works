# wap to print the even numbers from 1 to n

n = int(input("Enter a number: "))

for i in range(1,n+1):               #We gave n+1 cause it will exclude the last value
    
    if i % 2 != 0:
        
        print(i)