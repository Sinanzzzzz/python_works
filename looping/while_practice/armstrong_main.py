
num = int(input("Enter a number: "))

temp = num

sum = 0

length = len(str(num))

while(num > 0):
    
    digit = num % 10
    sum += digit ** length
    num //= 10

if sum == temp:
    print("The number is armstrong")
else:
    print("The number is not armstrong")