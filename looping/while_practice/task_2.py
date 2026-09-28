# wap to print the even numbers from 1 to n

i = 1
n = int(input("Enter the number:"))  #Assume a value(eg:30)

while(i <= n):
    if i % 2 == 0:
        print(i)
    i += 1
    