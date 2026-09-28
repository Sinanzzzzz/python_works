# wap to get the product of odd digits of the number

num = int(input("Enter a number: "))

product = 1

while(num>0):
    digit = num % 10
    if digit % 2 != 0:
        product *= digit
    
    num //= 10

print(f"The product of odd digits of the number = {product}")