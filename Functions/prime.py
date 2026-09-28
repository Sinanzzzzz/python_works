# wap to check a number is prime or not

def is_prime(num):
    
    if num<2:
        print(f"{num} is not a prime number")
    else:
        for i in range(2,num):
            
            if num % i == 0:
                
                print(f"{num} is not prime")
                break
        else:
            print(f"{num} is prime")
        
is_prime(1)