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

def results(player_input):
    def play(list):
        return choice(list)
    computer_play = play(moves)

    if player_input == computer_play:
        sleep(1)
        print(computer_play)
        sleep(0.8)
        print('How boring.')
        sleep(1)
        print('Tied.')
    else:
        if player_input == rock:
            if computer_play == paper:
                sleep(1)
                print(computer_play)
                sleep(0.8)
                print('Paper covers rock.')
                sleep(1)
                print('You lose.')
            elif computer_play == scissors:
                sleep(1)
                print(computer_play)
                sleep(0.8)
                print('Rock crushes scissors.')
                sleep(1)
                print('You won!')
                
        elif player_input == paper:
            if computer_play == scissors:
                sleep(1)
                print(computer_play)
                sleep(0.8)
                print('Scissors cuts paper.')
                sleep(1)
                print('You lose.')
            elif computer_play == rock:
                sleep(1)
                print(computer_play)
                sleep(0.8)
                print('Paper covers rock.')
                sleep(1)
                print('You won!')

        elif player_input == scissors:
            if computer_play == rock:
                sleep(1)
                print(computer_play)
                sleep(0.8)
                print('Rock crushes scissors.')
                sleep(1)
                print('You lose.')
            elif computer_play == paper:
                sleep(1)
                print(computer_play)
                sleep(0.8)
                print('Scissors cuts paper.')
                sleep(1)
                print('You won!')

replay = True
while replay == True:
    player_move = int(input('Type 0 for Rock, 1 for Paper and 2 for Scissors: '))
    
    if player_move == 0: 
        player_move = rock
    elif player_move == 1: 
        player_move = paper
    elif player_move == 2: 
        player_move = scissors
    else: print('Invalid input, you lose.')

    sleep(0.8); print(f'You play:\n{player_move}')
    sleep(1); print('And the computer plays', end ='')
    sleep(0.8); print('.', end ='')
    sleep(0.8); print('.', end ='')
    sleep(0.8); print('.')

    if player_move in moves:
        results(player_move)
    else:
        print('Better luck next time.')

    replay = input('\nDo you want to play again? Type 1 for Yes: ')
    if replay == '1':
        replay = True
    else:
        replay = False
