#1. Create a program that tells us how many days, weeks and months
#we have left if we live until 90 years old.
age = 90 - int(input('Type your age: '))

print(f'You have {age * 365} days, {age * 52} weeks, and {age * 12} months left.')
