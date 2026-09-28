# wap to get the count of odd numbers from 1 to n

i = 1
n = int(input("Enter a number: "))
count = 0
while(i<=n):
    if i % 2 != 0:
        count += 1
    i += 1
print(f"The count of odd numbers from 1 to {n} = {count}")