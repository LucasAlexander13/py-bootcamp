from random import randint
from game_art import *

print(logo)
print('Welcome to the Number Guessing Game!')

number = randint(1, 100)
print('I\'m thinking of a number between 1 and 100.')

difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

guessing = True
while guessing:
    print(f'You have {attempts} attempts remaining to guess the number.')
    guess = int(input('Make a guess: '))

    if guess == number:
        print(f'You got it! The number was {number}')
        print(win)
        guessing = False

    elif guess < number:
        print(low)
        attempts -= 1
        
    elif guess > number:
        print(high)
        attempts -= 1
    
    if attempts == 0:
        print('You\'ve run out of guesses...')
        print(lose)
        guessing = False
    else:
        print('Guess again.\n')
    
