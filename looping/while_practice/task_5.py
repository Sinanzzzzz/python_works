# wap to the print the cube of odd numbers from  n to m

n = int(input("Enter the starting number: "))
m = int(input("Enter the ending number: "))

while(n <= m):
    if n % 2 != 0:
        print(n**3)
    n += 1