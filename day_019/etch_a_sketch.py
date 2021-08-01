from turtle import Turtle, Screen

tim = Turtle()
screen  = Screen()

def move_forward(): #w key
    tim.forward(15)

def move_backward(): #s key
    tim.backward(15)

def turn_right(): #d key
    tim.right(5)

def turn_left(): #a key
    tim.left(5)

