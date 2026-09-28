num = int(input("Enter a number: "))

if num>0:
    print(f"{num} is a positive number")
elif num==0:
    print(f"{num} is neither positive nor negative")
else:
    print(f"{num} is a negative number")