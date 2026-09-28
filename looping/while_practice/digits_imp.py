# wap to get the total digits in the number given

number = int(input("Enter a number:"))
count = 0

while(number>0):
    number = number // 10
    count += 1
    
print(f"The total digits in the number = {count}")