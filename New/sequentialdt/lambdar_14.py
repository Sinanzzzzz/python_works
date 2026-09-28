# Reduce
# Product of list using reduce()

l = [1,2,3,4]

import functools

print(functools.reduce(lambda x,y:x*y,l))