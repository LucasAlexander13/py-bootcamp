from random import choice

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
    studying = True; score = 0
    name = input('Enter your name: ').title()
    
    if name == 'None':
        break

    while studying:
        char = choice(list(hangul))

        if input(f'{char}: ').upper() == hangul[char]:
            print(f'Very good, {name}!')
            score += 1
        else:
            print(f'You missed. You final score was {score} points.')
            studying = False
