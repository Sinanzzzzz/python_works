# Write a program to create a list of 5 random 3 digit numbers

import random

num = [random.randint(100,1000) for i in range(5)]
print(num)

# OR
# import random

# num = list(random.randint(100,1000) for i in range(5))
# print(num)