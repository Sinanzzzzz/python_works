# wap to check the number if it is Armstrong or not

number = 153
sum = 0
temp = number                # We use the temp variable because the value of number gets 
                             # changed inside the while loop
while(number > 0):
    digit = number % 10
    sum += digit ** 3
    number //= 10

if sum == temp:
    print("The number is armstrong")
else:
    print("The number is not armstrong")    