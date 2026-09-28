# 3. Given 2 lists
# l1 = [13,27,30,42,57]
# l2 = [13,57,89,33,80]
# Find the common elements

l1 = [13,27,30,42,57]
l2 = [13,57,89,33,80]

s1 = set(l1)                # We can find intersection only if it is set,so convert list
s2 = set(l2)                # to set

print(list(s1.intersection(s2)))  #list ilottu convert aakum
