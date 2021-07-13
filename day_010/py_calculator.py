logo = """
 _____________________
|  _________________  |          +                   -                    x                   / 
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 1 | 2 | 3 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 7 | 8 | 9 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|          ^                   %                   //                  sqr 
"""

def sum(a, b): return a + b
def subtraction(a, b): return a - b
def multiply(a, b): return a * b
def division(a, b): return a / b
def power(a, b): return a ** b
def remainder(a, b): return a % b
def integer(a, b): return a // b
def square(a, b): return a ** (1 / b)

operations = {
    '+': sum,
    '-': subtraction,
    'x': multiply,
    '*': multiply,
    '/': division,
    '^': power,
    '%': remainder,
    '//': integer,
    'sqr': square,
}

print(logo)

f_number = int(input('Enter a number: '))
symbol = input('Enter an operation: ')
l_number = int(input('Enter another number: '))

operation = operations[symbol]
answer = operation(f_number, l_number)

print(f'\n{f_number} {symbol} {l_number} = {answer}\n')

while True:
    replay = input(f'Type \'y\' to continue calculating with {answer}: ')
    if replay.lower() != 'y':
        break

    symbol = input('Pick an operation: ')
    o_number = int(input('Enter another number: '))

    operation = operations[symbol]
    new_answer = operation(answer, o_number)

    print(f'\n{answer} {symbol} {o_number} = {new_answer}\n')

    answer = new_answer
