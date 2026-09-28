# Print numbers where from 1 to 100
# Number == (Sum of digits)^2

for num in range(1,101):
    sum = 0
    while(num > 0):
        digit = num % 10
        sum += digit
        num = num // 10
    
    print(sum**2)