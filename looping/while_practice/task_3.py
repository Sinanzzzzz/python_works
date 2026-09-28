# wap to print the even numbers from n to m

n = int(input("Enter the starting number: "))
m = int(input("Enter the ending number: "))

while(n <= m):
    if n % 2 == 0:
        print(n)
    n += 1
    