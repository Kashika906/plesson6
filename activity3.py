

weight = float(input("Enter your weight (kg): "))
height_cm = float(input("Enter your height (cm): "))

height = height_cm / 100   

bmi = weight / (height * height)

print("Your BMI is:", round(bmi, 2))

if bmi <= 18.5:
    print("Underweight")
elif bmi <=25:
    print("Healthy")
elif bmi <= 30:
    print("Overweight")
elif bmi <= 35:
    print("Obese")
else:
    print("Severely Obese")