# wap to check if the number is positive even number
 
num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print(f"{num} is a positive even number")
else:
    print(f"{num} is a not positive even number")