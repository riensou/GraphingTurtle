import math
import re

def terminate(ErrorMessage):
    print('Error: ' + ErrorMessage)
    quit()

def is_integer(int_string):
    return int_string.isnumeric() or (int_string[0] == '-' and int_string[1:].isnumeric())

# Eventually add special forms 
# sin, cos, tan
# csc, sec, cot
# ln, log_(10)(100) = 2
# !, sum_(k=1)^(10)(x*k^2+3)

def is_valid_func(func_string):
    """Checks whether or not func_string can be properly parsed and evaluated as a function"""

    if not func_string:
        terminate('Missing function')

    if not re.match('[\(\)\+\*\-\^/0-9x]+', func_string): # How does re.match work?
        terminate('Invalid character(s)') # Why does is_valid_func('-m') get by this check?

    if re.search('[A-Za-wyz]', func_string): # Temporary, remove when adding special forms
        terminate('Invalid variable(s)')

    if re.search('x[0-9]', func_string):
        terminate('Invalid coefficient order')

    if re.match('[\+\*\)\^/]', func_string[0]):
        terminate('Invalid operation location')

    if len(list(re.findall('\(', func_string))) != len(list(re.findall('\)', func_string))):
        terminate('Unbalanced parenthesis')

    if re.search('\(\)', func_string):
        terminate('Empty parenthesis')

    if re.search('\^', func_string):
        if len(list(re.findall('\^\(', func_string))) != len(list(re.findall('\^', func_string))):
            terminate('Exponents require parenthesis')

    if len(func_string) > 1:
        if func_string[0:2] == '--':
            terminate('Double negative')
        if func_string[0] == '-':
            is_valid_func(func_string[1:])
        


def func_parser(func):
    """
    Turns a string expression into a list of tokens. 
    Calls helper on the tokens to get a callable Python function.

    >>>func_parser(x + 2)(4)
    6
    >>>func_parser(x^(2))(3)
    8
    >>>func_parser((x + 3)^(2))(1)
    16
    >>>func_parser(3^x)(2)
    9
    """
    is_valid_func(func)
    func = func.replace(' ', '') # removes whitespace
    tokens = [element for element in list(re.split('(\d*)', func)) if element]

    i = 0
    while i < len(tokens) - 1:
        if re.match('\d*', tokens[i]) and tokens[i + 1] == '(':
            tokens.insert(i + 1, '*')
            i += 1
        elif tokens[i] == ')' and re.match('\d*', tokens[i + 1]): # This is not working.
            tokens.insert(i + 1, '*')
            i += 1
        i += 1

    return tokens # for testing
    # return helper(tokens)

def helper(tokens):

    # Base case: one term left
    if len(tokens) == 1:
        if is_integer(tokens[0]):
            return lambda x: int(tokens[0]) # constant term
        else:
            return lambda x: x # variable term

    # Order of Operations:
    #                       Parenthesis
    #                       Exponents
    #                       Multiplication
    #                       Division
    #                       Addition
    #                       Subtraction

    if '(' in tokens:
        # Case 1: '(' is at the beginning of the list
        # Case 2: '(' is after a number being distributed
        4

print(func_parser('4((x + 3)3)5')) # This works, but more complex functions don't.

# Look into converting infix list of tokens to prefix ?
    

    