# wap to get the count of even digits from the number given

number  = int(input("Enter a number: "))
count = 0

while(number>0):             # Important condition
    digit = number % 10      # For getting last digit
    if digit % 2 == 0:
        count += 1
    number = number // 10    # For eliminating number 

print(f"The count of even digits = {count}")