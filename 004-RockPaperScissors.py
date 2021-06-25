from random import choice
from time import sleep

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

player_move = int(input('Type 0 for Rock, 1 for Paper and 2 For Scissors: '))
if player_move == 0: player_move = rock
elif player_move == 1: player_move = paper
elif player_move == 2: player_move = scissors
else: print('Invalid input, you lose.')


def results(player_input):
    def play(list):
        return choice(list)
    computer_play = play(moves)
    if player_input == computer_play:
        sleep(0.8)
        print(computer_play)
        sleep(0.8)
        print('Draw.')
    else:
        if player_input == rock:
            if computer_play == paper:
                sleep(0.8)
                print(computer_play)
                sleep(0.8)
                print('You lose.')
            elif computer_play == scissors:
                sleep(0.8)
                print(computer_play)
                sleep(0.8)
                print('You won!')
        elif player_input == paper:
            if computer_play == scissors:
                sleep(0.8)
                print(computer_play)
                sleep(0.8)
                print('You lose.')
            elif computer_play == rock:
                sleep(0.8)
                print(computer_play)
                sleep(0.8)
                print('You won!')
        elif player_input == scissors:
            if computer_play == rock:
                sleep(0.8)
                print(computer_play)
                sleep(0.8)
                print('You lose.')
            elif computer_play == paper:
                sleep(0.8)
                print(computer_play)
                sleep(0.8)
                print('You won!')

print('You play:')
print(player_move)
sleep(0.8)
print('And the computer plays', end ='')
sleep(0.8)
print('.', end ='')
sleep(0.8)
print('.', end ='')
sleep(0.8)
print('.')

if player_move in moves:
    results(player_move)
else:
    print('Better luck next time.')
