# Check whether a number is divisible by 3 or 7

num = int(input("Enter a three digit number: "))

if num%3==0 or num%7==0:
    print(f"{num} is divisible by 3 or 7")
else :
    print(f"{num} is not divisible by 3 or 7")