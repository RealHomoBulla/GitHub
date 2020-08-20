'''Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words(words: list):
    pass
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"'''

from functools import wraps

def censorship(some_list=['pepsi', 'BMW']):
  def inner_decorator(func):
    print(f'Decorating function "{func.__name__}"...')
    @wraps(func)
    def wrap(*args, **kwargs):
      decorated_str = func(*args, **kwargs)
      for word in some_list:
        decorated_str = decorated_str.replace(word, '*')
      print(decorated_str)
      return decorated_str
    return wrap
  return inner_decorator

@censorship()
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'

create_slogan('Mike')


@censorship(some_list=['drinks', 'brand'])
def another_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'

another_slogan('Carl')
