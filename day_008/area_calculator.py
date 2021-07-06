from random import randint

'''
You are painting a wall. The instructions on the paint can 
says that 1 can of paint can cover 5 square meters of 
wall. Given a random height and width of wall, calculate 
how many cans of paint you'll need to buy.
'''

def area_calc(height, width):
    total_can = (height * width) / 5
    return print(f'{total_can}')

area_calc(randint(1, 10), randint(1, 10))
