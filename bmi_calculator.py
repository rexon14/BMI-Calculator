weight = float(input("Input your weight (kg): "))
height = float(input("Input yout height (m) : "))
BMI = weight/(height**2)

print("Your Body Mass Index: {0}\n".format(BMI))

if (BMI < 18.5):
    print("Category: Underweight")
    
elif (BMI >= 18.5) and (BMI < 25):
    print("Category: Normal weight")
    
elif (BMI >= 25) and (BMI < 30):
    print("Category: Overweight")
    
elif (BMI >= 30) and (BMI < 35):
    print("Category: Obese")
    
else:
    print("Category: Clinically Obese")
