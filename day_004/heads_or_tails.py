from random import randint

'''
You are going to write a virtual coin toss program. 
It will randomly tell the user "Heads" or "Tails".
'''

coin = randint(0, 1)
if coin == 0:
    coin = 'Heads'
else:
    coin = 'Tails'

print(f'You roll {coin}')
