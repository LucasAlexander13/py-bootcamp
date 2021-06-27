'''
You are going to write a program that calculates 
the average studentheight from a List of heights.
'''

students_heights = input('Enter the heights separated by space: ').split(' ')

heights_sum = 0
quantity = 0
for height in students_heights:
    heights_sum += int(height)
    quantity += 1

average_height = heights_sum / quantity

print(f'The avarage height of students is: {int(average_height)}')
