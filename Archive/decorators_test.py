import time


def time_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {(end_time - start_time)*1000} miliseconds to execute.')
        return res
    return wrapper


# @time_function
def square_numbers(some_list):
    new_list = []
    for num in some_list:
        new_list.append(num ** 2)
    return  new_list

# @time_function
def cubed_numbers(some_list):
    new_list = []
    for num in some_list:
        new_list.append(num ** 2)
    return  new_list



test_list = [1,2,3,4,5,6]
test_list_squared = square_numbers(test_list)
test_list_cubed = cubed_numbers(test_list)
# print(test_list_squared )
# print(test_list_cubed)
# decorated_function(test_list)



def first_decorator(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@first_decorator
def test():
    '''test function docs'''
    print('inner test function')
    return None

# print(test.__doc__)
# help(test)
test()

print(test.__name__)