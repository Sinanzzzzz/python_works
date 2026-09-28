# Prime number

number = int(input("Enter a number: "))

while(number <= 1):
    number = int(input("Enter a number above one: "))
    
for i in range(2,number):
    
    if number % i == 0:
        print("The number is not prime")
        break          # We use break because we have already found a divisor, so there is no need to check the remaining numbers
else:
    print("The number is prime")