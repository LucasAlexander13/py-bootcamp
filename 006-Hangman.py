from random import choice
from hangman_words import word_list
from hangman_art import *

'''
Randomly choose a word from the word_list and assign it to a 
variable called chosen_word. Ask the user to guess a letter and assign
their answer to a variable called guess. Make guess lowercase.
Check if the letter the user guessed (guess) is one of the letters 
in the chosen_word.
'''

chosen_word = choice(word_list)
letter_list = []
display = ''
lives = 6
victory = 0

for letter in chosen_word:
    display += '_'

print(computer, logo)

while lives != 0 and victory != 1:
    print(stages[lives])
    print(display.replace('', ' ')[1:-1].upper())
    guess = input('\nGuess a letter: ').lower()

    if guess in letter_list:
        print(f'"{guess}" was already tried, try another one.\n')

    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                letter_list.append(guess)

                display = display[:position] + guess + display[position + 1:]

                if display == chosen_word:
                    print(display.replace('', ' ')[1:-1].upper())
                    print(f'\nYou won the game. The word was: {chosen_word}.\n')
                    victory = 1
    else:
        
        print(f'"{guess}" is not in the chosen word.\n')
        letter_list.append(guess)
        lives -= 1
        if lives == 0:
            print(stages[0])
            print(f'Out of lives. The word was: {chosen_word}.\n')
