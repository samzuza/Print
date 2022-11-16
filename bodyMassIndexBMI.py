weight = float(input("Enter weight in pounds: "))

height = float(input("Enter height in inches: "))

KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254

weightInKilograms = weight * KILOGRAMS_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)

print("BMI is", bmi)

if bmi < 18.5:
    print(" underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else: print("obese")