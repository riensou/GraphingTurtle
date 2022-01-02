import math
import re

def terminate(ErrorMessage):
    print('Error: ' + ErrorMessage)
    quit()

def is_integer(int_string):
    return int_string.isnumeric() or (int_string[0] == '-' and int_string[1:].isnumeric())

def is_valid_func(func_string):
    if not func_string:
        terminate('Missing function')
    if not re.match('[\(\)\+\*\-\^/0-9x]+', func_string):
        terminate('Invalid character(s)') 
    if re.search('[A-Za-wyz]', func_string):
        terminate('Invalid variable(s)')
    if re.search('x[0-9]', func_string):
        terminate('Invalid coefficient order')
    if re.match('[\+\*\)\^/]', func_string[0]):
        terminate('Invalid operation character')
    if len(func_string) > 1:
        if func_string[0:2] == '--':
            terminate('Double negative')
        if func_string[0] == '-':
            is_valid_func(func_string[1:])
        

def func_parser(func):
    """
    Turns a string expression into a callable Python function

    >>>func_parser(x + 2)(4)
    6
    >>>func_parser(x^(2))(3)
    8
    >>>func_parser((x + 3)^ 2)(1)
    16
    >>>func_parser(3^x)(2)
    9
    """
    is_valid_func(func)
    func = func.replace(' ', '') # removes whitespace

    # Base case: one term left
    if len(func) == 1:
        if re.match('[0-9]', func):
            return lambda x: int(func)
        else:
            return lambda x: x


print(func_parser(input()))
