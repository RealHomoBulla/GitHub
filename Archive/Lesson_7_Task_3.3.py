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

list_of_args = []

def input_inspector(input_to_check):
    for i in range(len(input_to_check)):
        if '-' in str(input_to_check[i]) or '.' in str(input_to_check[i]) or str(input_to_check[i]).isdigit():
            if str(input_to_check[i]).replace('-', '').isdigit() == False:
                print(f'Only numbers are valid input for an arithmetical operation. "{i}" was not included.')
                continue
            list_of_args.append(float(input_to_check[i]))
        else:
            print(f'Only numbers are valid input for an arithmetical operation. "{i}" was not included.')
            continue


def take_input():
    operator_input = input('Please, enter a valid operator (+ - * / ):  ').replace(' ', '')
    numbers_input = input('Please, enter arguments, separated by comma: ').replace(' ', '').split(',')
    input_inspector(numbers_input)
    first_number = list_of_args[0]
    rest_of_numbers = list_of_args[1:]
    return (operator_input, first_number, rest_of_numbers)

operator, arg1, *args = take_input()
print(operator, arg1, *args)


def make_operation(operator, arg1, *args):

    # input_inspector(arg1)
    if '-' in str(arg1) or '.' in str(arg1) or str(arg1).isdigit():
        result = float(arg1)
    else:
        'Sorry, the first argument is incorrect. '
    print(f'argument {arg1} was added ')
    for arg in args:
        if type(arg) == list:
            for n in range(len(arg)):
                if '-' in str(n) or '.' in str(n) or str(n).isdigit():
                    list_of_args.append(float(arg[n]))
                    print(f'argument {arg[n]} was added ')
        elif '-' in str(arg) or '.' in str(arg) or str(arg).isdigit():
            list_of_args.append(float(arg))
            print(f'argument {arg} was added ')
        else:
            print(f'Only numbers are valid input for an arithmetical operation. "{arg}" was not included.')
            continue
    print(list_of_args)

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

# make_operation('*', 7, 6)
make_operation(operator,arg1, *args)

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
