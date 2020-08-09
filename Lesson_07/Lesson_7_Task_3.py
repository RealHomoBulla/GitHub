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

# This function will verify, if input is valid or not. Valid input will be saved to a list, invalid declined.
def input_inspector(input_to_check):
    if type(input_to_check) == int or type(input_to_check) == float:
        list_of_args.append(float(input_to_check))
    # Input can be a list or tuple (args), it should check and save all valid data inside lists to our calculation.
    elif type(input_to_check) == list or type(input_to_check) == tuple:
        for i in range(len(input_to_check)):
            # All numbers, including negative and decimals will be checked
            if '-' in str(input_to_check[i]) or '.' in str(input_to_check[i]) or str(input_to_check[i]).isdecimal():
                # I had some bug with accidental extra spaces, numbers were not added properly.
                if str(input_to_check[i]).replace('-', '').isdigit() == False or str(input_to_check[i]).replace('-', '').isdecimal() == False:
                    # Some input can be with "-" or ".", but not a number. E.g. "-x" would raise error, I fixed it.
                    continue
                # If input is okay, it will be added to calculation
                list_of_args.append(float(input_to_check[i]))
    else:
        print('Sorry, you have to enter valid numbers!')

# This function will perform calculation. You can call take_input() before to get user input
# or you can call it directly with required arguments. Examples below.
def make_operation(operator, arg1, *args):
    # If you pass it pre-input data:
    if len(list_of_args) > 0:
        result = arg1
        input_inspector(args)
    else:
        # If you use it directly, without pre-input data:
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
        # It will handle division by Zero
        if 0 in list_of_args:
            print('You are not allowed to divide by Zero!')
            quit()
        for i in list_of_args[1:]:
            result /= i
        # Also, it will round any division to 2nd decimal place.
        print(round(result, 2),)

    # Also, it will handle wrong operator input.
    if operator.strip() not in "+-*/":
        print('Sorry, wrong operator. Try again.')
        quit()


# So, to call it with input, we need to create operator and expression Variables with take_input() function call.
operator_input, input_to_check = take_input()
# Then we pass input data to our input_inspector()
input_inspector(input_to_check)
# and it stores valid numbers in list_of_args, we can slice it  and get  arg1, *args
arg1 = list_of_args[0]
args = list_of_args[1:]
# and we call the function, finally.
make_operation(operator_input, arg1, args)


# I wanted to make it possible to create function with and without pre-input data. Clear the list, and call it now:
list_of_args = []
make_operation('+', 7, 7, 2)

# Works for negative numbers as well.
list_of_args = []
make_operation('-', 5, 5, -10, -20)

list_of_args = []
make_operation('*', 6, 7)

# Division is rounding to 2nd decimal place.
list_of_args = []
make_operation('/', 100, 10, 3)

# And division by zero error is handled as well.
list_of_args = []
make_operation('/', 100, 10, 0)