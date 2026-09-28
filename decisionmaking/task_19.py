# Bonus 5. Check whether a number is positive and divisible by 4.

num = int(input("Enter a digit number: "))

if num>0 and num%4==0:
    print(f"{num} is positive and divisible by 4")
else:
    print(f"{num} is either not positive or not divisible by 4")