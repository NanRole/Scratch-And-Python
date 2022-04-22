height = float(input('Please enter your height (cm): '))
weight = float(input('Please enter your weight (kg): '))
BMI = weight / (height / 100) ** 2
print('Your BMI is', BMI)