from random import choice
from os import system
from time import sleep
from art_variables import hangul_study

def clear(time):
    sleep(time)
    system('cls')


hangul = {
    'training': { # 10 points
        'ㅏ': 'A',
        'ㅓ': 'Ó',
        'ㅗ': 'O',
        'ㅜ': 'U',
        'ㅡ': 'UH',
        'ㅣ': 'I',
        'ㅔ': 'E',
        'ㅐ': 'É',
    },
    'easy': { # 20 points
        'ㅑ': ['YA','IA'],
        'ㅕ': ['YÓ','IÓ'],
        'ㅛ': ['YO','IO'],
        'ㅠ': ['YU','IU'],
        'ㅖ': ['YE','IE'],
        'ㅒ': ['YÉ','IÉ'],
    },
    'normal': { # 30 points
        'ㅘ': 'OA',
        'ㅝ': 'UÓ',
        'ㅟ': 'UI',
        'ㅚ': 'UE',
        'ㅞ': 'UÉ',
        'ㅙ': 'OÉ',
        'ㅢ': 'UHI'
    },
    'moderate': { # 40 points

    },
    'hard': { # 50 points

    },
    'hardest': { # 60 points

    },
    'insane': { # 70 points

    }
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
        if input(f'{char}: ').upper() in hangul[char]:
            print(f'Very good, {name}!')
            score += 1
            clear(1)
        else:
            print(f'You missed. You final score was {score} points.')
            print(f'{char} = {hangul[char].title()}. Type Enter to restart: ', end='')
            input()
            studying = False
