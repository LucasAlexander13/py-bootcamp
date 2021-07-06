from math import ceil

'''
You are painting a wall. The instructions on the paint can 
says that 1 can of paint can cover 5 square meters of 
wall. Given a random height and width of wall, calculate 
how many cans of paint you'll need to buy.
'''

def area_calc(height, width):
    total_can = (height * width) / 5
    return print(f'You will need {ceil(total_can)} cans of paint.')

wall_height = float(input('Enter the height of the wall: '))
wall_width = float(input('Enter the width: '))

area_calc(wall_height, wall_width)
