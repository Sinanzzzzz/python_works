#wap to check the given number is divisible by 3 and 5
number = int(input("Enter a number: "))

if number % 3 == 0:
    
    if number % 5 == 0:
        
        print(f"{number} is divisble by 3 and 5")
        
    else:
        print(f"{number} is divisible by 3 but not 5")
        
else:
        print(f"{number} is not divisible by 3")