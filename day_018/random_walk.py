from turtle import Screen, Turtle, exitonclick
from random import choice

def move_up():
    tim.color(choice(color))
    tim.setheading(90)
    tim.forward(30)

def move_left():
    tim.color(choice(color))
    tim.setheading(180)
    tim.forward(30)

def move_down():
    tim.color(choice(color))
    tim.setheading(270)
    tim.forward(30)

def move_right():
    tim.color(choice(color))
    tim.setheading(0)
    tim.forward(30)

def clear():
    tim.reset()
    tim.pen(pensize=10)
    tim.speed('fastest')

tim = Turtle()
screen = Screen()
tim.shape('circle')
tim.pen(pensize=10)
tim.speed('fastest')

direction = [0, 90, 180, 270]
color = ['black','orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']

screen.listen()
screen.onkey(move_up, 'w')
screen.onkey(move_left, 'a')
screen.onkey(move_down, 's')
screen.onkey(move_right, 'd')
screen.onkey(clear, 'c')
screen.onkey(screen.bye, 'x')

while True:
    try:
        tim.color(choice(color))
        tim.setheading(choice(direction))
        tim.forward(30)
    except:
        break
