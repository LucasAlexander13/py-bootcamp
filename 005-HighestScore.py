'''
You are going to write a program that calculates
the highest score from a List of scores.
'''

students_score = input('Enter the scores separated by spaces: ').split(' ')
highest = 0

for score in students_score:
    if int(score) > highest:
        highest = int(score)

print(f'The highest score in the class is: {highest}.')
