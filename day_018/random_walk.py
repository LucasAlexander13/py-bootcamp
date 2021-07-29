from turtle import Screen, Turtle
from random import choice

tim = Turtle()
screen = Screen()
tim.shape('circle')
tim.pen(pensize=10)
tim.speed('fastest')

direction = [0, 90, 180, 270]
color = ['black','orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']

while True:
    tim.color(choice(color))
    tim.setheading(choice(direction))
    tim.forward(30)
