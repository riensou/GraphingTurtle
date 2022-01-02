from terminal_query import *
import turtle

turtle.setworldcoordinates(-5, -5, 5, 5)

window = turtle.Screen()
celine = turtle.Turtle()

def draw_axis():
    """Draw both the x and y axis"""
    t = turtle.Turtle()
    t.goto(x_max, 0)
    t.goto(x_min, 0)
    t.goto(0, y_max)
    t.goto(0, y_min)

window.mainloop()
