
def logger(func):
  '''function which decorates other function'''
  print(f'Decorated function {func.__name__}')
  def wrapper(*args, **kwargs):
    print('test')
    result = func(*args, **kwargs)
    print(f'Function {func.__name__} was called with parameters {args} and {kwargs}.')
    return result
  return wrapper


@logger
def summing(a, b):
  print('test inside summing func')
  return a + b
