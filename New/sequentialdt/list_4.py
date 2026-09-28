# Find the largest number without using built in method

l = [23,45,67,12,90,78]

max = l[0]

for i in l:
    
    if i>max:
        max = i
print("Largest number is:",max)

min = l[0]

for i in l:
    
    if i<min:
        min = i
print("Smallest number is:",min)