'''
Your job is to write a program that allows you to mark a square on the map 
using a two-digit system. The first digit is the vertical column number 
and the second digit is the horizontal row number.
'''

def call(list):
    index = 0
    print('     1    2    3')

    for row in list:
        print(f'{(index + 1):^3}{list[index]}')
        index += 1

row1 = ['_', '_', '_']
row2 = ['_', '_', '_']
row3 = ['_', '_', '_']

map = [row1, row2, row3]
call(map)

treasure = int(input('Where do you want to hide the treasure: '))

row = (treasure // 10) 
column = (treasure % 10) 
map[row - 1][column - 1] = 'X'

call(map)
