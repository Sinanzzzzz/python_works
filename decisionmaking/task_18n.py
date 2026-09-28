# Largest of Three Numbers: Print the largest or All Numbers are Equal if all equal

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

if num_1==num_2 and num_2==num_3:
    print("All numbers are Equal")
elif num_1>=num_2 and num_1>=num_3:
    print(f"{num_1} is the largest")
elif num_2>=num_1 and num_2>=num_3:
    print(f"{num_2} is the largest")
else:
    print(f"{num_3} is the largest")