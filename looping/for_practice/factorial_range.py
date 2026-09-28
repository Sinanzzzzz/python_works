# get the factorial of numbers from 2 to 6

for num in range(2,7):
    
    product = 1
                                #nested for loop (first edukkunna 2 adiyil poi range 1 to 2 pokum(baaki noraml)) ithellam oru valya for loop il koduthu(last cheytha problem)
    for i in range(1,num+1):    #1,2,3,4
        
        product *= i
        
    print(f"The factorial of {num} = {product}")