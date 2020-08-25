'''Task 2
Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function'''

def in_range(*args):
    lst = []
    # If there is only one argument, it means it must be "stop" argument, starting from 0 and step is 1.
    if len(args) == 1:
        # Start from 0:
        number = 0
        # Incrementing the number while "stop" value is reached.
        while number < args[0]:
            # Filling the list one by one until condition is met.
            lst.append(number)
            number += 1
    elif len(args) == 2:
        number = args[0]
        while number < args[1]:
            lst.append(number)
            number += 1
    elif len(args) == 3:
        number = args[0]
        # For a normal positive step:
        if args[0] < args[1]:
            while number < args[1]:
                lst.append(number)
                number += args[2]
        # For a negative step:
        elif args[0] > args[1]:
            while number > args[1]:
                lst.append(number)
                number += args[2]
    else:
        raise TypeError(f'range expected at most 3 arguments, got {len(args)}')
    return lst

# Works with only one argument.
for i in in_range(10):
    print(i)

print('')

# Works with two arguments.
for i in in_range(1, 10):
    print(i)

print('')

# Works with step argument, and with negative step as well.
for i in in_range(100, -10, -10):
    print(i)

# Gives an error if there is no arguments, or if there is more than 3 arguments, same as original "range" fucntion.
# for i in in_range():
#     print(i)

# for i in in_range(1, 10, 1, 1):
#     print(i)

