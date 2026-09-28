# 1. Given a list l = [1,2,2,3,4,4,5,6]
# Create a new dictionary where keys are numbers
# and values are number occurrence of each number.

l = [1,2,2,3,4,4,5,6]

# new = {i:l.count(i) for i in l}         # Combination syntax
# print(new)

new = {}
for i in l:
    new[i]=l.count(i)
print(new)