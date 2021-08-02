from turtle import Turtle, Screen
from color import color
from random import choice

tim = Turtle()
tim.shape('arrow')
tim.pen(pensize=10)
screen  = Screen()

def move_forward(): #w key
    tim.color(choice(color))
    tim.forward(30)

def move_backward(): #s key
    tim.color(choice(color))
    tim.backward(30)

def turn_right(): #d key
    tim.right(30)

def turn_left(): #a key
    tim.left(30)

def clear_screen(): #c key
    tim.reset()
    tim.pen(pensize=10)

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_right, 'd')
screen.onkey(turn_left, 'a')
screen.onkey(clear_screen,'c')

screen.exitonclick()
