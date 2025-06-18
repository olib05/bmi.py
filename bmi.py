import time


print("Hello. Welcome to my BMI and BMR calculator!")


height = float(input("Enter your height in cm: ")) 
weight = float(input("Enter your weight in kg: "))
age = int(input("Enter your age in years: "))
isMale = str(input("Are you male? (y/n): "))
activity = str(input("What is your activity level? (No Exercise/Light Excercise/Moderate Excercise/Very Active/Extra Active): "))


bmi = weight / (height/100)**2
   
print(f"Your BMI is {bmi:.1f}")


if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi <= 34.9:
    print("You are severely over weight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")


if isMale:
    bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
else:
    bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)


if activity == "no excercise":
    print(f"Your daily intake should be {bmr * 1.2:.2f} calories.")
elif activity == "light excercise":
    print(f"Your daily intake should be {bmr * 1.375:.2f} calories.")
elif activity == "moderate excercise":
    print(f"Your daily intake should be {bmr * 1.55:.2f} calories.")
elif activity == "very active":
    print(f"Your daily intake should be {bmr * 1.725:.2f} calories.")
elif activity == "extra active":
    print(f"Your daily intake should be {bmr * 1.9:.2f} calories.")


print(f"Your BMR is {bmr:.2f}")


time.sleep(5)