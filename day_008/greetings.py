'''
Write a program that call a function called greet and 
that prints three lines of greetings to the user.  
'''

def greet():
    print('Welcome to my greeting program.')
    name = input('Please, tell me your name: ')
    print(f'Welcome {name}! It\'s nice to see you here.')

greet()
