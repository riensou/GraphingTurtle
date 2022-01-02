import turtle

window = turtle.Screen()
celine = turtle.Turtle()

def draw_axis(rotation):
    t = turtle.Turtle()
    t.left(rotation)
    t.forward(max(window.window_width(), window.window_height()) / 2)
    t.backward(max(window.window_width(), window.window_height()))

draw_axis(0) # x-axis
draw_axis(90) # y-axis

