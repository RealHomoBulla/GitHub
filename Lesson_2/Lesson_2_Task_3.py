"""
Task 3
Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
"""

# I wanted to make it a loop-program to perform many operations until User wishes to quit.
# The best way I see it is to use While-Loop.
while True:
    print('At any moment you can type "Q" or "q" to quit the Program.')

# Input data
    arg1 = input('Enter Argument 1:\n').strip()
    # Strip removes accidental spaces.

    # I added Quit Option which can stop the program.
    if arg1 == 'Q' or arg1 == 'q':
        break

    # Now it will check if User give a digit or not, and if so - digit is saved to Variable.
    # Also, it was required to allow negative and decimal numbers.
    elif '-' in arg1 or '.' in arg1 or arg1.isdigit():
        arg1 = float(arg1)

    else:
        print('Sorry, invalid argument. Try again.')
        continue


    operator = input('Enter a valid operator:\n + for Addition\n - for Subtraction\n * for Multiplication\
    \n / for Division\n** for Exponent (power of...)\n % for Modulus\n// for Floor Division\n').strip()
    if operator == 'Q' or operator == 'q':
        break
    if operator not in '+-*/**%//':
        print(f'Invalid operator "{operator}". Try again with operator from a list.')
        continue


    arg2 = input('Enter Argument 2:\n').strip()
    if arg2 == 'Q' or arg2 == 'q':
        break
    elif '-' in arg2 or '.' in arg2 or arg2.isdigit() == True:
        arg2 = float(arg2)

        # Here i wanted debug the ZeroDivisionError, but making it possible to still use '0' as a second argument for any other calculations.
        if arg2 == 0 and operator in '/%//':
            print('You can\'t divide by Zero! Try again.')
            continue
    else:
        print('Sorry, invalid argument. Try again.')
        continue


    result = None

    # Logic for every possible input
    if operator == '+':
        result = arg1 + arg2
    elif operator == '-':
        result = arg1 - arg2
    elif operator == '*':
        result = arg1 * arg2
    elif operator == '/':
        result = arg1 / arg2
    elif operator == '**':
        result = arg1 ** arg2
    elif operator == '%':
        result = arg1 % arg2
    elif operator == '//':
        result = arg1 // arg2

    # Output data
    if not result is None:
        print(f'Result: {arg1} {operator} {arg2} = {round(result, 2)}')

    # There was a bug which didn't give any output in case if Result was equal to '0' due to result = None construction.
    # This lines were intended to fix this but.
