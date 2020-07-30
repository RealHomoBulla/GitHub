'''Task 3
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.

For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  '''

list_of_args = []

# This  function takes operator and user input (if it may be required to pass into function)
def take_input():
    operator_input = input('Please, enter a valid operator (+ - * / ):  ').replace(' ', '')
    input_to_check = input('Please, enter arguments, separated by comma: ').replace(' ', '').split(',')
    return (operator_input,  input_to_check)


def input_inspector(input_to_check):
    if type(input_to_check) == int or type(input_to_check) == float:
        list_of_args.append(float(input_to_check))
    elif type(input_to_check) == list or type(input_to_check) == tuple:
        for i in range(len(input_to_check)):
            if '-' in str(input_to_check[i]) or '.' in str(input_to_check[i]) or str(input_to_check[i]).isdecimal():
                if str(input_to_check[i]).replace('-', '').isdecimal() == False:
                    continue
                list_of_args.append(float(input_to_check[i]))

def make_operation(operator, arg1, *args):
    if len(list_of_args) > 0:
        result = arg1
        input_inspector(args)
    else:
        input_inspector(arg1)
        result = arg1
        input_inspector(args)



    if operator == '+':
        for i in list_of_args[1:]:
            result += i
        print(result)

    if operator == '-':
        for i in list_of_args[1:]:
            result -= i
        print(result)

    if operator == '*':
        result = 1
        for i in list_of_args[:]:
            result *= i
        print(result)

    if operator == '/':
        if 0 in list_of_args:
            print('You are not allowed to divide by Zero!')
            quit()
        for i in list_of_args[1:]:
            result /= i
        print(round(result, 2),)



operator_input, input_to_check = take_input()
input_inspector(input_to_check)
arg1 = list_of_args[0]
args = list_of_args[1:]

make_operation(operator_input, arg1, args)

list_of_args = []
make_operation('+', 7, 7, 2)

list_of_args = []
make_operation('-', 5, 5, -10, -20)

list_of_args = []
make_operation('*', 6, 7)

list_of_args = []
make_operation('/', 100, 10, 3)

list_of_args = []
make_operation('/', 100, 10, 0)