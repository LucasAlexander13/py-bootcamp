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

def clear_screen(): #c key
    tim.reset()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_right, 'd')
screen.onkey(turn_left, 'a')
screen.onkey(clear_screen,'c')

screen.exitonclick()
