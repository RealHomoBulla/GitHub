
from functools  import wraps



def first_decorator(func):
    @wraps(func)
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@first_decorator
def test():
    '''test function docs'''
    print('inner test function')


# print(test.__doc__)
# help(test)
# test()
#
# print(test.__name__)


def add_brake_log(size=2):
    def inner_dec(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            for _ in range(size):
                print('_'*80)
            func(*args, **kwargs)
            for _ in range(size):
                print('_' * 80)
        return wrap
    return inner_dec


@add_brake_log(size=2)
def test():
    '''test function docs'''
    print('inner test function')
# test()

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return 'Function will not run'
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return 'Function is running'

can_run  = True
print(func())

can_run = False
print(func())

# Authorization

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not  auth or not  check_auth(auth.username, auth.password):
            authenticate()
        return  f(*args, **kwargs)
    return decorated
