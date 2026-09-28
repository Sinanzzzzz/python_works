

def check_spy(num):
    s = str(num)

    sum = 0
    product = 1

    for i in s:
        sum = sum + int(i)
        product = product * int(i)

    if sum == product:
        print("Spy number")
    else:
        print("Not a spy number")
        
n=int(input("Enter a number:"))        
check_spy(n)