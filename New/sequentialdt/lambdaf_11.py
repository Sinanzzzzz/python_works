# Filter even values greater than 50
l = [23,45,67,12,89,70]

print(list(filter(lambda x:x%2==0 and x>50,l)))