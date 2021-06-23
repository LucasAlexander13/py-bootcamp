'''
Congratulations, you've got a job at Python Pizza. 
Your first job is to build an automatic pizza order program.
'''
print('''Welcome to Pyzza, the Python pizza delivery.
"S" for Small Pizza: $15
"M" for Medium Pizza: $20
"L" for Large Pizza: $25
''')

size = input('Enter the size you wish: ')

print('\nAnswer the follow questions with "Y" for Yes and "N" for no.\n')
pepperoni = input('Extra pepperoni: ')
cheese = input('Extra cheese: ')

if size == 'S':
    price = 15
    if pepperoni == 'Y':
        price += 2
    if cheese == 'Y':
        price += 1
elif size == 'M':
    price = 20
    if pepperoni == 'Y':
        price += 3
    if cheese == 'Y':
        price += 1
elif size == 'L':
    price = 25
    if pepperoni == 'Y':
        price += 3
    if cheese == 'Y':
        price += 2
else:
    print('Sorry, we don\'t work with that.')

print(f'Your final bill is: ${price:.2f}')
