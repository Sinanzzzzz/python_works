# wap to get the perfect numbers from a given range of 1 to 1000

for num in range(1,1001):
    
    sum = 0

    for i in range(1,num):    #first find the perfect number ,then the range
        
        if num % i == 0:
            
            sum += i
    if sum == num:        
        print("Perfect",num)
