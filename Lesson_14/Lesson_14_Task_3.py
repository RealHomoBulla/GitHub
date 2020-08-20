'''Task 3
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
def arg_rules(type_: type, max_length: int, contains: list):
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'''

from functools import wraps

def arg_rules(type_, max_length, contains):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      for arg in args:
        if type(arg) is not type_:
            print('Wrong type')
            return False
        if len(arg) > max_length:
            print('Very long')
            return False
        for item in contains:
            if item not in arg:
                print('Doesn\'t contain some of required symbols')
                return False
      print(func(*args, **kwargs))
      return func(*args, **kwargs)
    return wrapper
  return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
  '''This function prints some text with name...'''
  return f"{name} drinks pepsi in his brand new BMW!"


create_slogan('fjkladsjgkjlkasdgjlkadsjkl')
create_slogan('ldskj')
create_slogan(1)
create_slogan('pavel05@g.com')

print(create_slogan.__name__)
print(create_slogan.__doc__)