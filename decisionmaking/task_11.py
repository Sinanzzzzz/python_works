num = int(input("Enter a number: "))

if num%2==0:
    if num>=2 and num<=5:
        print("Not Weird")
    elif num>=6 and num<=20:
        print("Weird")
    elif num>20:
        print("Not Weird")
else :
    print("Weird")
    
"""
Hacker Rank
OR
if num%2==1:
    print("Weird")
elif num%2==0 and num>=2 and num<=5:
    print("Not Weird")
elif num%2==0 and num>=6 and num<=20:
    print("Weird")
else :
    print("Not Weird")
"""

  