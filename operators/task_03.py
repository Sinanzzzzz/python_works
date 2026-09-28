"""
Ask for the total price of the bill, then ask how 
many diners there are. Divide the total bill by the 
number of diners and show how much each 
person must pay.
"""

#Asks user to enter the total bill
total_price=int(input("Enter the total price:"))

#Asks user to enter how many diners are there
people=int(input("Enter the count of diners:"))

amount=total_price/people

print(f"Everyone should pay {amount}")