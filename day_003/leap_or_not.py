'''
Write a program that works out whether if a given year is a leap year.
'''
year = int(input('Enter a year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap!')
        else:
            print('Not leap.')
    else:
        print('Leap.')
else:
    print('Not leap.')
