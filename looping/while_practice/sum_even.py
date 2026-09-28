# wap to get the sum of even digits of the number

num = int(input("Enter a number: "))

sum = 0

while(num>0):
    digit = num % 10
    if digit % 2 == 0:
        sum += digit
        
    num //= 10
print(f"The sum of even digits of the number = {sum}")