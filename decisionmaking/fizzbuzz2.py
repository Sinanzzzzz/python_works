number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is both divisible by 3 and 5")
elif number % 3 == 0 or number % 5 == 0:
    print(f"{number} is either divisible by 3 or 5")
else:
    print(f"{number} is not divisible by 3 or 5")