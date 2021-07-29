from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.shape('turtle')
tim.speed('slow')
tim.color('dark green', 'green')

shape_side = 3
shape_angle = 360 / shape_side

for shapes in range(7):

    for sides in range(shape_side):
        tim.forward(50)
        tim.right(shape_angle)

    shape_side += 1
    shape_angle = 360 / shape_side