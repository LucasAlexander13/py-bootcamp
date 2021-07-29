from turtle import Screen, Turtle
from time import sleep

tim = Turtle()
screen = Screen()
tim.shape('turtle')

for i in range(4):
    sleep(1)
    tim.forward(75)
    tim.left(90)
