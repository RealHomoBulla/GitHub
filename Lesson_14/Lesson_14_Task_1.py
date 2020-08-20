'''Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
"add called with 4, 5"

def logger(func):
  pass
@logger
def add(x, y):
  return x + y
@logger
def square_all(*args):
  return [arg ** 2 for arg in args]'''

from functools import wraps

def logger(func):
  '''function which decorates other function'''
  print(f'Decorating function "{func.__name__}"...')
  @wraps(func)
  def wrapper(*args, **kwargs):
    '''wrapper docstring will not be shown'''
    result = func(*args, **kwargs)
    print(f'Function {func.__name__} was called with parameters {args}.')
    return result
  
  return wrapper


@logger
def summing(a, b):
  '''This function summs 2 numbers "a" and "b"'''
  return a + b

summing(4, 5)
print(f'Function name is "{summing.__name__}".')
print(f'Function docstring is: \'{summing.__doc__}.\'')
