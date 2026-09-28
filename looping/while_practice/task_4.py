# wap to print the square of even numbers from 1 to n

i = 1
n = int(input("Enter the number: "))

while(i <= n):
    if i % 2 == 0:
        print(i**2)
    i += 1