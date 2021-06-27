#1. write a program that get a two digit number and returns it's sum.
number = int(input('Type a two digit number: '))
sum = (number // 10) + (number % 10)

print(f'The sum is {sum}.')
