weight_kg = float(input("Enter your weight(kg): "))
height_m = float(input("Enter your height(m): "))

bmi = weight_kg/(height_m**2)
print(f"Your BMI value = {bmi}")

if bmi<18.5:
    print("You are underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("You are normal")
elif bmi>=25.0 and bmi<=29.9:
    print("You are overweight")
else:
    print("Obesity")
