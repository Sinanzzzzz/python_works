salary = int(input("Enter your salary: "))

if salary==50000:
    bonus=salary * 20/100   
    total=salary+bonus          #Or direclty print(f"Your total salary is {bonus + salary}") 
    print(f"Your total salary is {total}")    
    
elif salary==30000:
    bonus=salary * 10/100
    total=salary+bonus
    print(f"Your total salary is {total}")
    
elif salary<30000:
    bonus=salary * 5/100
    total=salary+bonus
    print(f"Your total salary is {total}")
else:
    print("Thank you")