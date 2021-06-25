'''
Your job is to write a program that allows you to mark a square on the map 
using a two-digit system. The first digit is the vertical column number 
and the second digit is the horizontal row number.
'''
column1 = ['1', '2', '3']
column2 = ['4', '5', '6']
column3 = ['7', '8', '9']
map = [column1, column2, column3]

index = 0
for colum in map:
    print(map[index])
    index += 1

