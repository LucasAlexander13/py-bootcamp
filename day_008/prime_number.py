'''
You need to write a function that checks whether if the 
number passed into it is a prime number or not.
'''

def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(prime(int(input('Enter a number: '))))
