'''z
Task 1
Write a function called oops that explicitly raises an IndexError exception when called.
Then write another function that calls oops inside a try/except state­ment to catch the error.
What happens if you change oops to raise KeyError instead of IndexError?'''

def oops():
    print('Oops. There must be some error.')
    raise IndexError
    # If we change it to KeyError nothing will change because any error can be raised this way.
    # It will be indicating same lines of codes and only name of raised error will change.

def div_func(arg1, *args):
    result = arg1
    try:
        for n in args:
            result /= n
        return(f'Result equals to {round(result, 2)}.')
    except:
        oops()

# Not raising an Error.
x = div_func(100, 10, 3)
print(x)
print()

# Raising an Error, but instead of ZeroDivisionError raises IndexError
x = div_func(100, 10, 0)
print(x)