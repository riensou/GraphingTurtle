print('Welcome to GraphingTurtle. Enter anything to continue.')
input()

# Define bounds
print('Choose a minimum x value.')
x_min = input()
if x_min.isnumeric():
    x_min = int(x_min)

    print('Choose a maximum value.')
    x_max = input()
    if x_max.isnumeric() and int(x_max) > x_min:
        x_max = int(x_max)

        print('Choose a minimum y value.')
        y_min = input()
        if y_min.isnumeric():
            y_min = int(y_min)

            print('Choose a maximum y value.')
            y_max = input()
            if y_max.isnumeric() and int(y_max) > y_min:
                y_max = int(y_max)
            else:
                print('Error: Invalid Response')
        else:
            print('Error: Invalid Response')
    else:
        print('Error: Invalid Response')
else:
    print('Error: Invalid Response')