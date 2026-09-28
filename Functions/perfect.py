# define a function to check the given number is perfect or not

def is_perfect(num):
    
    sum = 0
    for i in range(1,num):
        
        if num % i == 0:
            sum += i

    print(f"{num} is a perfect number" if sum == num else f"{num} is not a perfect number")
        
is_perfect(6)