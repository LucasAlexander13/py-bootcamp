from time import sleep

def clear():
    return print("\033c", end='')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = {}

while True:
    sleep(1)
    print(logo)
    sleep(1)
    print('Welcome to the secret auction program.')
    name = input('Enter your name: ').title()
    bid = float(input('Type your bid: $'))

    bidders[name] = bid

    another = input('Are there any other bidders? Type "yes" or "no": ')
    sleep(1)

    if another.lower() == 'yes':
        clear()
    else:
        clear()
        break

higher_bid = 0
winner = 'no one'

for name in bidders:
    sleep(1)
    print(f'{name} made the bid of ${bidders[name]:.2f}')

    if bidders[name] > higher_bid:
        higher_bid = bidders[name]
        winner = name     

print(f'The winner was {winner}, with a bid of {higher_bid:.2f}')
