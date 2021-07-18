from random import choice
from os import system
from time import sleep
from art_variables import hangul_study

def clear(time):
    sleep(time)
    return system('cls')

def get_hangul(score):
    if score <= 10:
        char = choice(list(hangul['training']))
        return char
    elif score <= 20:
        char = choice(list(hangul['easy']))
        return char
    elif score <= 30:
        char = choice(list(hangul['normal']))

def level(score):
    if score <= 10:
        return 'training'
    elif score <= 20:
        return 'easy'
    elif score <= 30:
        return 'normal'

hangul = {
    'training': { # 10 points
        'ㅏ': 'A',
        'ㅓ': 'Ó',
        'ㅗ': 'O',
        'ㅜ': 'U',
        'ㅡ': 'UH',
        'ㅣ': 'I',

    },
    'easy': { # 20 points
        'ㅔ': 'E',
        'ㅐ': 'É',
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
    print(hangul_study)
    name = input('Enter your name: ').title()
    
    if name == 'None':
        break
    else:
        score = 0
        clear(0.5)

    while True:
        print(hangul_study)
        print(f'Current score: {score} points')

        char = get_hangul(score)
        current = hangul[level(score)][char]

        if input(f'{char}: ').upper() in current:
            print(f'Very good, {name}!')
            score += 1
            clear(1)
        else:
            print(f'You missed. You final score was {score} points.')
            print(f'You are in {level(score)} level.')
            print(f'{char} = {current}. Type Enter to restart: ', end='')
            input()
            break
