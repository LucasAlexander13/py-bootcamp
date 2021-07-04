'''
You need to write a function that checks whether if the 
number passed into it is a prime number or not.
'''

def prime():
    number = int(input('Enter a number: '))
    for i in range(2, number):
        if number % i == 0:
            return print('It is not a prime number.') 
    return print('It is a prime number.')

prime()
