# Write a program to find the position of a character in a string

# s = input("Enter a string:")
# char = input("Enter a character:")

# a=s.find(char)
# print(a)

s = input("Enter a string:")
char = input("Enter a character:")

if char in s:
    print(s.index(char))
else:
    print("Character is not present")