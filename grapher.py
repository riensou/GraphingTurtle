import turtle

x_min = -10
y_min = -10
x_max = 10
y_max = 10

turtle.setworldcoordinates(-5, -5, 5, 5)

window = turtle.Screen()
celine = turtle.Turtle()

# Draw both the x and y axis
def draw_axis(axis):
    t = turtle.Turtle()
    if axis == 'x':
        t.goto(x_max, 0)
        t.goto(x_min, 0)
    else:
        t.goto(0, y_max)
        t.goto(0, y_min)
draw_axis('x')
draw_axis('y')

window.mainloop()
