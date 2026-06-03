weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))
bmi = weight/(height*height)
print("BMI =", round(bmi, 2))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")