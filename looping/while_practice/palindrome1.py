# wap to reverse the number entered by user

number = int(input("Enter a number: "))
temp = number                              #We use temp cause the the value inside the 
reverse = 0                                # "number" will changed in the loop

while(number>0):
    digit = number %10
    reverse = reverse * 10 + digit              
    number = number // 10                      
    
if temp == reverse:
    print("Palindrome")
else:
    print("Not palindrome")