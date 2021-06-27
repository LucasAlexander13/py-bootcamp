'''
You are going to write a program that calculates the sum of all 
the even numbers from 1 to 100. Thus, the first even number 
would be 2 and the last one is 100:
'''
number = 1
sum = 0
while number <= 100:
    if number % 2 == 0:
        sum += number
        number += 1
    else:
        number += 1

print(f'The sum of even numbers until 100 is: {sum}')
