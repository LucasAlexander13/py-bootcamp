from turtle import Turtle, Screen

tim = Turtle()
screen  = Screen()

def move_forward(): #w key
    tim.forward(15)

def move_backward(): #s key
    tim.backward(15)

def turn_right(): #d key
    tim.right(15)

def turn_left(): #a key
    tim.left(15)

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)

screen.exitonclick()
