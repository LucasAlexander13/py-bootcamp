from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.shape('turtle')
tim.speed('slowest')

intern_angle = 60
shape_angle = 180 - intern_angle
shape_side = 3

for shapes in range(8):
    for sides in range(shape_side):
        tim.forward(30)
        tim.right(shape_angle)
    shape_side += 1
    intern_angle += 30
    shape_angle = 180 - intern_angle
        
