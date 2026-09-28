# Three Digit Number: Check whether a number is between 100 and 999

num = int(input("Enter a three digit number: "))

if num>=100 and num<=999:
    print(f"{num} is a three digit number")
else:
    print(f"{num} is not a three digit number")