# wap to get the sum of even numbers and product of odd numbers from 1 to n

i = 1
n = int(input("Enter a number: "))
sum = 0
product = 1

while(i<=n):
    if i % 2 == 0:
        sum += i
        
    else:
        product *= i
    i += 1
    
print(f"The sum = {sum} and product = {product} ")