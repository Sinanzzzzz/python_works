# Print all automorphic numbers (numbers whose square ends with the number itself, e.g., 5 → 25, 6 → 36, 25 → 625).

num = int(input("Enter a number: "))
length = 1                  #for single digit

square = num**2

if square % (10 ** length) == num:
    print("The number is automorphic")
else:
    print("The number is not automorphic")
    