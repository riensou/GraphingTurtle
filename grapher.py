from terminal_query import *
import turtle

turtle.setworldcoordinates(x_min, y_min, x_max, y_max)

window = turtle.Screen()
celine = turtle.Turtle()
celine.penup()

def draw_axis():
    """Draw both the x and y axis"""
    t1 = turtle.Turtle()
    t1.goto(2 * x_max, 0)
    t1.goto(2 * x_min, 0)
    t2 = turtle.Turtle()
    t2.goto(0, 2 * y_max)
    t2.goto(0, 2 * y_min)
draw_axis()

celine.goto(x_min, func(x_min))
celine.pendown()

while celine.xcor() <= x_max:
    try:
        celine.goto(celine.xcor() + 0.1, func(celine.xcor() + 0.1))
    except:
        # failed attempt at resolving 1 / x
        celine.penup()
        celine.goto(celine.xcor() + 0.1, func(celine.xcor() + 0.1))
        celine.pendown()

window.mainloop()
