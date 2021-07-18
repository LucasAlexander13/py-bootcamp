from random import choice
from os import system
from time import sleep
from art_variables import hangul_study

def clear(time):
    sleep(time)
    return system('cls')

def get_hangul(score):
    global revised
    if score <= 10:
        char = choice(list(hangul['training']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char
    elif score <= 20:
        char = choice(list(hangul['easy']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char
    elif score <= 30:
        char = choice(list(hangul['normal']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char

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
        '아': 'A',
        '어': 'Ó',
        '오': 'O',
        '우': 'U',
        '으': 'UH',
        '이': 'I',

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
        '에': 'E',
        '애': 'É',
        '야': ['YA','IA'],
        '여': ['YÓ','IÓ'],
        '요': ['YO','IO'],
        '유': ['YU','IU'],
        '예': ['YE','IE'],
        '얘': ['YÉ','IÉ'],
    },
    'normal': { # 30 points
        'ㅘ': 'OA',
        'ㅝ': 'UÓ',
        'ㅟ': 'UI',
        'ㅚ': 'UE',
        'ㅞ': 'UÉ',
        'ㅙ': 'OÉ',
        'ㅢ': 'UHI',
        '와': 'OA',
        '워': 'UÓ',
        '위': 'UI',
        '외': 'UE',
        '웨': 'UÉ',
        '왜': 'OÉ',
        '의': 'UHI'
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
        revised = []
        clear(0.5)

    while True:
        print(hangul_study)
        print(f'Current score: {score} points')

        char = get_hangul(score)
        current = hangul[level(score)][char]

        if input(f'{char}: ').upper() in current:
            print(f'Very good, {name}!')
            score += 1
            clear(0.5)
        else:
            print(f'You missed. You final score was {score} points.')
            print(f'{char} = {current}. Type Enter to restart: ', end='')
            input()
            break
