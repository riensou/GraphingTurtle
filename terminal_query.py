from function_parser import *

print('Welcome to GraphingTurtle. Enter anything to continue.')
input()

# Define bounds
print('Choose a minimum x value.')
x_min = input()
if x_min and is_integer(x_min):
    x_min = int(x_min)

    print('Choose a maximum x value.')
    x_max = input()
    if x_max and (is_integer(x_max) and int(x_max) > x_min):
        x_max = int(x_max)

        print('Choose a minimum y value.')
        y_min = input()
        if y_min and is_integer(y_min):
            y_min = int(y_min)

            print('Choose a maximum y value.')
            y_max = input()
            if y_max and (is_integer(y_max) and int(y_max) > y_min):
                y_max = int(y_max)
            else:
                terminate('Invalid y_max')
        else:
            terminate('Invalid y_min')
    else:
        terminate('Invalid x_max')
else:
    terminate('Invalid x_min')

# Enter function, y(x)
print('Choose a function to graph.')
func = string_to_func(input('y = '))