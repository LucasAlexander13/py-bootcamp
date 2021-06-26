from random import choice

'''
Randomly choose a word from the word_list and assign it to a 
variable called chosen_word. Ask the user to guess a letter and assign
their answer to a variable called guess. Make guess lowercase.
Check if the letter the user guessed (guess) is one of the letters 
in the chosen_word.
'''

word_list = ['dinosaur', 'spider', 'github', 'airplane', 'volcano']
chosen_word = choice(word_list)
letter_list = []
hangman = ''
lives = 5
victory = 0

for letter in chosen_word:
    hangman += '_'

while lives != 0 and victory != 1:
    print(hangman)
    guess = input('\nGuess a letter: ').lower()

    if guess in letter_list:
        print('That letter was already tried, try another.\n')

    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                letter_list.append(guess)

                hangman = hangman[:position] + guess + hangman[position + 1:]

                if hangman == chosen_word:
                    print(f'You won the game. The word was: {chosen_word}.\n')
                    victory = 1
    else:
        print(f'"{guess}" is not in the chosen word.\n')
        letter_list.append(guess)
        
        lives -= 1
        if lives == 0:
            print(f'Out of lives. The word was: {chosen_word}.\n')
