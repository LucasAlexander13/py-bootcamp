'''
Create a program that tells us how many days, weeks and months
we have left if we live until 90 years old.
'''
age = 90 - int(input('Type your age: '))
left = [age * 365, age * 52, age * 12]
print(f'You have {left[0]} days, {left[1]} weeks, and {left[2]} months left.')
