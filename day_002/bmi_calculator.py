#1. Write a program that calculates the Body Mass Index from a user.
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))
#2. The BMI is calculated by dividing the weight by the square of the height.
BMI = (weight) / (height ** 2)
#3. Warning you should convert the result to a whole number.
print(f'Your BMI is {int(BMI)}')
