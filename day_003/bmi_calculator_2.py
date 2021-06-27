'''
Write a program that calculates the Body Mass Index from a user.
It should tell them the interpretation of their BMI based on the BMI value.
'''
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))

BMI = (weight) / (height ** 2)
print(f'Your BMI is {BMI:.2f}')

if BMI < 18.5:
    print('And you are underweight.')
elif BMI < 25:
    print('And you have a normal weight.')
elif BMI < 30:
    print('And you are slightly overweight.')
elif BMI < 35:
    print('And you are obese.')
else:
    print('And you are clinically obese.')
