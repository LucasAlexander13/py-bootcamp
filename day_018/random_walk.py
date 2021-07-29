from turtle import Screen, Turtle
from random import choice

tim = Turtle()
screen = Screen()
tim.shape('circle')
tim.pen(pensize=10)
tim.speed('fastest')

direction = {
    'right': 90,
    'forward': 0,
    'back': 180,
    'left': -90
}
color = ['black','orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']

while True:
    random_dir = choice(list(direction))
    
    tim.color(choice(color))
    tim.right(direction[random_dir])
    tim.forward(30)
