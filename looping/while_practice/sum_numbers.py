# wap to get the sum of numbers from 1 to n

i = 1
n = int(input("Enter a number: "))
sum = 0         # For showing that sum is an integer
while(i<=n):
    sum += i
    i += 1
print(f"The sum of numbers from 1 to {n} = {sum}")