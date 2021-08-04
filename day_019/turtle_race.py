from my_turtles import turtles, screen
from random import choice
from time import sleep

guess = screen.textinput('Make your bet',  'Which turtle will win the run?: ')

while True:

    chosen_turtle = choice(turtles)
    chosen_turtle.forward(10)
    if chosen_turtle.xcor() == 180:
        sleep(1)
        chosen_turtle.write('I win', align='left')
        sleep(2)
        if chosen_turtle.color() == guess:
            chosen_turtle.write('And you win too', align='left')
        else:
            chosen_turtle.write('But you lose', align='left')
        break

screen.exitonclick()
