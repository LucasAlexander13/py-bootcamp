from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.shape('turtle')
tim.speed('slowest')

for i in range(4):
    for i in range(5):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)
    tim.left(90)
