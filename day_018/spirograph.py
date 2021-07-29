from turtle import Screen, Turtle
from random import choice

tim = Turtle()
screen = Screen()
tim.shape('circle')
tim.pen(pensize=1)
tim.speed('fastest')

color = ['black','orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']

for i in range(72):
    tim.color(choice(color))
    tim.circle(100)
    tim.left(5)

tim.pen(pensize=1.5)
for i in range(24):
    tim.color(choice(color))
    tim.circle(100)
    tim.left(15)