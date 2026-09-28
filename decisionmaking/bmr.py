weight_kg = int(input("Enter your weight(kg): "))
height_cm = int(input("Enter your height(cm): "))
age = int(input("Enter your age: "))

bmr = (10*weight_kg) + (6.25*height_cm) - (5*age) + 5
print(bmr)