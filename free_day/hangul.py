from random import choice
from os import system
from time import sleep
from art_variables import hangul_study

def clear(time):
    sleep(time)
    return system('cls')

def get_hangul(score):
    global revised
    if score <= 11:
        char = choice(list(hangul['training']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char
    elif score <= 27:
        char = choice(list(hangul['easy']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char
    elif score <= 41:
        char = choice(list(hangul['normal']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char
    elif score <= 57:
        char = choice(list(hangul['moderate']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char
    elif score <= 67:
        char = choice(list(hangul['hard']))
        if char in revised:
            char = get_hangul(score)
        else:
            revised.append(char)
        return char

def get_level(score):
    '''Pega o número da pontuação e retorna o nível de conhecimento em hangul'''
    if score <= 11:
        return 'training'
    elif score <= 27:
        return 'easy'
    elif score <= 41:
        return 'normal'
    elif score <= 57:
        return 'moderate'
    elif score <= 67:
        return 'hard'

hangul = {
    'training': { # 10 points
        'ㅏ': ['A'],
        'ㅓ': ['Ó'],
        'ㅗ': ['O'],
        'ㅜ': ['U'],
        'ㅡ': ['UH'],
        'ㅣ': ['I'],
        '아': ['A'],
        '어': ['Ó'],
        '오': ['O'],
        '우': ['U'],
        '으': ['UH'],
        '이': ['I'],

    },
    'easy': { # 20 points
        'ㅔ': ['E'],
        'ㅐ': ['É'],
        'ㅑ': ['YA','IA'],
        'ㅕ': ['YÓ','IÓ'],
        'ㅛ': ['YO','IO'],
        'ㅠ': ['YU','IU'],
        'ㅖ': ['YE','IE'],
        'ㅒ': ['YÉ','IÉ'],
        '에': ['E'],
        '애': ['É'],
        '야': ['YA','IA'],
        '여': ['YÓ','IÓ'],
        '요': ['YO','IO'],
        '유': ['YU','IU'],
        '예': ['YE','IE'],
        '얘': ['YÉ','IÉ'],
    },
    'normal': { # 30 points
        'ㅘ': ['OA'],
        'ㅝ': ['UÓ'],
        'ㅟ': ['UI'],
        'ㅚ': ['UE'],
        'ㅞ': ['UE'],
        'ㅙ': ['OÉ'],
        'ㅢ': ['UHI'],
        '와': ['OA'],
        '워': ['UÓ'],
        '위': ['UI'],
        '외': ['UE'],
        '웨': ['UE'],
        '왜': ['OÉ'],
        '의': ['UHI']
    },
    'moderate': { # 40 points
        'ㄱ': ['KA'],
        'ㄴ': ['NA'],
        'ㄷ': ['TA'],
        'ㄹ': ['RA'],
        'ㅁ': ['MA'],
        'ㅂ': ['BA'],
        'ㅅ': ['SA'],
        'ㅈ': ['DJA'],
        '가': ['KA'],
        '나': ['NA'],
        '다': ['TA'],
        '라': ['RA'],
        '마': ['MA'],
        '바': ['BA'],
        '사': ['SA'],
        '자': ['DJA']

    },
    'hard': { # 50 points
        'ㄲ': ['KA'],
        'ㄸ': ['TA'],
        'ㅃ': ['PA'],
        'ㅆ': ['SA'],
        'ㅉ': ['TCHA'],
        '까': ['KA'],
        '따': ['TA'],
        '빠': ['PA'],
        '싸': ['SA'],
        '짜': ['TCHA']

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
    
    if name == '':
        break
    else:
        score = 0
        revised = []
        clear(0.5)

    while True:
        print(hangul_study)
        print(f'Current score: {score} points')

        char = get_hangul(score)
        current = hangul[get_level(score)][char]

        if input(f'{char}: ').upper() in current:
            print(f'Very good, {name}!')
            score += 1
            clear(0.5)
        else:
            print(f'You missed. You final score was {score} points.')
            print(f'{char} = {current[0]}. Type Enter to restart: ', end='')
            input()
            break
