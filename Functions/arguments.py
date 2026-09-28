# define a function to get the sum of numbers:

def sum_numbers(*args):    # args = (3,4,5) iterable
    sum = 0
    for i in args:
        
        sum += i
        
    print(sum)
    
sum_numbers(3,4,5,6,7)