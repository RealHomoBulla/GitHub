# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def test_func():
    a = 10
    b =  15
    my_str = 'yo'
    hello = 'hello world'
    def inner_func():
        c = 15
    return

my_test = test_func

print(f'Function "{my_test.__name__}" has {my_test.__code__.co_nlocals} variables inside.')