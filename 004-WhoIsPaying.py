from random import randint
'''
You are going to write a program which will select a random name from a list
of names. The person selected will have to pay for everybody's food bill.
'''

names = input('Enter the names separated by comma and space: ').split(', ')

choice = randint(0, (len(names) - 1))
print(f'So {names[choice]}, you will pay the bill.')
