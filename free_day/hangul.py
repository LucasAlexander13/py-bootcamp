from random import choice
from os import system
from time import sleep
from art_variables import hangul_study

def clear(time):
    sleep(time)
    system('cls')

hangul = {
    'ㅏ': 'A',
    '아': 'A',
    'ㅓ': 'Ó',
    '어': 'Ó',
    'ㅗ': 'O',
    '오': 'O',
    'ㅜ': 'U',
    '우': 'U',
    'ㅔ': 'E',
    '에': 'E',
    'ㅐ': 'É',
    '애': 'É',
    'ㅡ': 'UH',
    '으': 'UH',
    'ㅣ': 'I',
    '이': 'I',
    'ㅑ': 'YA',
    '야': 'YA',
    'ㅕ': 'YÓ',
    '여': 'YÓ',
    'ㅛ': 'YO',
    '요': 'YO',
    'ㅠ': 'YU',
    '유': 'YU',
    'ㅖ': 'YE',
    '예': 'YE',
    'ㅒ': 'YÉ',
    '얘': 'YÉ',
}

while True:
    clear(0.5)
    studying = True; score = 0
    print(hangul_study)
    name = input('Enter your name: ').title()
    clear(0.5)
    
    if name == 'None':
        break

    while studying:
        char = choice(list(hangul))
        print(hangul_study)
        print(f'Current score: {score} points')
        if input(f'{char}: ').upper() == hangul[char]:
            print(f'Very good, {name}!')
            score += 1
            clear(1)
        else:
            print(f'You missed. You final score was {score} points.')
            studying = False
            clear(3)
