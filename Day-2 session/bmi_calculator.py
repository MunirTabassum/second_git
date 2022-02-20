height = float(input("What is your height in cm? "))
weight = float(input("What is your weight? "))
BMI = weight / (height/100)**2  # height divide by 100 to convert metres into cm
print("Your bmi is ", BMI)
