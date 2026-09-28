# Largest of Two Numbers: Take two numbers. Print the largest or Both are Equal

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_1>num_2:
    print(f"The largest number is {num_1}")
elif num_1<num_2:
    print(f"The largest number is {num_2}")
else:
    print("Both are equal")
