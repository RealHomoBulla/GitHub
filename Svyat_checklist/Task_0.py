'''0. Писать фугкцию принимающую позиционные, именованные и безлимитные параметры в разных вариантах.'''

def some_func(arg1, arg2):
    print('\nNormal arguments function: ')
    print(arg1)
    print(arg2)

# It should have exactly 2 arguments, no less and no more than 2.
some_func('hello', 'world')


def tuple_func(arg1, arg2, *args):
    print('\nTuple "args" function: ')
    print(arg1)
    print(arg2)
# If you print 'args' like this, they will be printed how they are, as a tuple.
    print(args)

tuple_func('hello', 'world', 'how', 'are', 'you?')


def unpack_func(arg1, arg2, *args):
    print('\nUnpacked "args" function: ')
    print(arg1)
    print(arg2)
# If you print 'args' like this, they will be unpacked and printed together.
    print(*args)

unpack_func('hello', 'world', 'how', 'are', 'you?')


zip_list = ['how', 'are', 'you?']
def zipped_func(arg1, arg2, *args):
    print('\nZipped "args" function: ')
    print(arg1)
    print(arg2)
# If you print 'args' like this, they will be unpacked and printed together, but you have to pass zipped list:
    for item in args:
        print(item)

zipped_func('hello', 'world', *zip_list)


example_dict = {'Key1' : 'Corvo Attano', 'Key2': 'Nerevarin', 'Key3': 'Emily Caldwin'}
def kwargs_one(**kwargs):
    print('\nUnpacking dictionary with **kwargs')
    for key, value  in kwargs.items():
        print(f'{key} : {value}')

kwargs_one(**example_dict)