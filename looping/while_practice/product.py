# wap to get the product of numbers from 1 to n

i = 1
num = int(input("Enter a number:"))
product = 1
while(i <= num):
    product *= i
    i += 1
print(f"The product of numbers from 1 to {num} = {product}")