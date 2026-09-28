# wap to get the second largest among three

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

if num_1 > num_2 and num_1 < num_3 or num_1 < num_2 and num_1 > num_3:
    print(f"{num_1} is the second largest number")
elif num_2 > num_1 and num_2 < num_3 or num_2 < num_1 and num_2 > num_3:
    print(f"{num_2} is the second largest number")
else:
    print(f"{num_3} is the second largest number")
    
# If the input is 3 2 4, the first condition of the 'if' statement becomes True
# because num_1 > num_2 and num_1 < num_3.

# If the input is 4 3 2, the second condition (after 'or') becomes True
# because num_1 < num_2 and num_1 > num_3
