'''Task 3
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.

For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  '''

import operator

def make_operation(operator, arg1, *args):

    if '-' in str(arg1) or '.' in str(arg1) or str(arg1).isdigit():
        result = float(arg1)
    else:
        'Sorry, the first argument is incorrect. '
    list_of_args = []


    for arg in args:
        if '-' in str(arg) or '.' in str(arg) or str(arg).isdigit():
            list_of_args.append(float(arg))

        else:
            print(f'Only numbers are valid input for an arithmetical operation. "{arg}" was not included.')
            continue


    if operator == '+':
        for i in list_of_args:
            result += i
        print(result)

    if operator == '-':
        for i in list_of_args:
            result -= i
        print(result)

    if operator == '*':
        for i in list_of_args:
            result *= i
        print(result)

    if operator == '/':
        for i in list_of_args:
            result /= i
        print(result)

make_operation('-', 5, 5, -10, '-20')

# if operator not in '+-*/':
#     print('Sorry, invalid operator. Use " + - * / "only. Try again.')
#
# else:
#     operator = {
#         '+': operator.add,
#         '-': operator.sub,
#         '*': operator.mul,
#         '/': operator.truediv
#     }
