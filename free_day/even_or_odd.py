last_number = int(input('Enter a number: '))

for number in range(1, last_number + 1):
    if number % 2 == 0:
        print(f'{number} is even.')
    else:
        print(f'{number} is odd.')
