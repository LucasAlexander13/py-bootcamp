from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()
tim.shape('turtle')
tim.speed('slow')

color = ['black', 'black', 'black', 'orange', 'dark orange', 'firebrick', 'dark red', 'crimson', 'medium violet red', 'dark magenta', 'medium orchid', 'medium purple', 'indigo', 'slate blue']

def draw_shape(shape_side):
    angle = 360 / shape_side
    for side in range(shape_side):
        tim.forward(100)
        tim.right(angle)

for shape in range(3, 10):
    tim.color(color[shape])
    draw_shape(shape)
