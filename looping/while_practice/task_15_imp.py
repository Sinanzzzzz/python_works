# wap to get the count of even and count of odd digit in a given number

number  = int(input("Enter a number: "))
count_even = 0
count_odd = 0

while(number>0):                    # Important condition
    digit = number % 10             # For getting last digit
    if digit % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    number = number // 10               # For eliminating number

print(f"The count of even digits = {count_even} and the count of odd digits = {count_odd}")