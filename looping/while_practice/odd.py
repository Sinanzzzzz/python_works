# wap to print the odd numbers from 1 to n

i = 1
n = int(input("Enter the number: "))
while(i <= n):
    if i % 2 != 0:       # or  i % 2 == 1(for checking odd)
        print(i)
    i += 1