'''Task 3
A simple calculator.

Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.

For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  '''



# Я извиняюсь, не успел доработать код и он получился запутанным.
# Я стремился сделать обработку неправильного ввода отдельной функцией, долго с этим провозился  и не успел
# реализовать все, что задумал и поредактировать код, уже пора сдавать задание.

list_of_args = []

def input_inspector(input_to_check):
    if type(input_to_check) == list or type(input_to_check) == tuple:
        for i in range(len(input_to_check)):
            if '-' in str(input_to_check[i]) or '.' in str(input_to_check[i]) or str(input_to_check[i]).isdigit():
                if str(input_to_check[i]).replace('-', '').isdigit() == False:
                    print(f'Only numbers are valid input for an arithmetical operation. "{input_to_check[i]}" was not included.')
                    continue
                list_of_args.append(float(input_to_check[i]))
    elif type(input_to_check) == int or type(input_to_check) == float:
        list_of_args.append(float(input_to_check))

    arg1 = list_of_args[0]
    args = list_of_args[1:]
    return (arg1, args)

def take_input():
    operator_input = input('Please, enter a valid operator (+ - * / ):  ').replace(' ', '')
    numbers_input = input('Please, enter arguments, separated by comma: ').replace(' ', '').split(',')
    print(numbers_input)
    return (operator_input, numbers_input)

def make_operation(operator, arg1, *args):
    result = 0
    if input_inspector(arg1):
        result += arg1
        print(result)
    else:
        print('You should enter number for the first argument.')
        quit()

    input_inspector(args)

    print(list_of_args)
    if operator == '+':
        for i in list_of_args[:]:
            result += i
        print(result)

    if operator == '-':
        for i in list_of_args[:]:
            result -= i
        print(result)

    if operator == '*':
        for i in list_of_args[1:]:
            result *= i
        print(result)

    if operator == '/':
        if 0 in list_of_args:
            print('You are not allowed to divide by Zero!')
            quit()
        for i in list_of_args[1:]:
            result /= i
        print(round(result, 2),)


operator, numbers_input = take_input()
arg1, args = input_inspector(numbers_input)

make_operation(operator,arg1, *args)

# make_operation('-', 5, 5, -10, -20)