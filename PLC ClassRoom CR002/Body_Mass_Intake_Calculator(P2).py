# Program to calculate Body Mass Index (BMI) and categorize it into different health categories(underweight, normal weight,overweight,obesity)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal weight"
elif bmi < 29.9:
    category = "Overweight"
else:
    category = "Obesity"

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
