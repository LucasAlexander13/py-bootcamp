from color import color
from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(500, 400)

sam = Turtle()
sam.shape('turtle')
sam.color(color[1])
sam.penup()
sam.setposition(-230, 60)

deb = Turtle()
deb.shape('turtle')
deb.color(color[3])
deb.penup()
deb.setposition(-230, 30)

tim = Turtle()
tim.shape('turtle')
tim.color(color[5])
tim.penup()
tim.setposition(-230, 0)

dom = Turtle()
dom.shape('turtle')
dom.color(color[7])
dom.penup()
dom.setposition(-230, -30)

bug = Turtle()
bug.shape('turtle')
bug.color(color[9])
bug.penup()
bug.setposition(-230, -60)

turtles = [sam, deb, tim, dom, bug]
guess = screen.textinput('Make your bet',  'Which turtle will win the run?: ')

while True:

    chosen_turtle = choice(turtles)
    chosen_turtle.forward(10)
    if chosen_turtle.xcor() ==  180:
        chosen_turtle.write('I win', align='left')
        if chosen_turtle.color() == guess:
            chosen_turtle.write('And you win too', align='left')
        else:
            chosen_turtle.write('But you lose', align='left')
        break



screen.exitonclick()
