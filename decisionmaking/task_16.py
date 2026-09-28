# Divisible by 5 or 10: Check whether a number is divisible by 5 or 10

num = int(input("Enter a three digit number: "))

if num%5==0 or num%10==0:
    print(f"{num} is divisible by 5 or 10")
else :
    print(f"{num} is not divisible by 5 or 10")