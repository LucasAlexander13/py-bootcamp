from turtle import Turtle, Screen

tim = Turtle()
screen  = Screen()

def move_up():
    tim.setheading(90)
    tim.forward(15)

def move_left():
    tim.setheading(180)
    tim.forward(15)

def move_down():
    tim.setheading(270)
    tim.forward(15)

def move_right():
    tim.setheading(0)
    tim.forward(15)

screen.listen()
screen.onkey(key='w', fun=move_up)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='s', fun=move_down)
screen.onkey(key='d', fun=move_right)

screen.exitonclick()
