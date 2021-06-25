'''
Your job is to write a program that allows you to mark a square on the map 
using a two-digit system. The first digit is the vertical column number 
and the second digit is the horizontal row number.
'''
column1 = ['_', '_', '_']
column2 = ['_', '_', '_']
column3 = ['_', '_', '_']
map = [column1, column2, column3]

index = 0
print('     1    2    3')
for column in map:
    print(f'{(index + 1):^3}{map[index]}')
    index += 1

treasure = int(input('Where do you want to hide the treasure: '))


