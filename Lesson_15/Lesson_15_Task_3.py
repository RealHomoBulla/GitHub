import functools

class TypeDecorators:

    @staticmethod
    def to_int(func):
        @functools.wraps(func)
        def call_int(*args, **kwargs):
            print('Covert to int')
            try:
                x = func(*args, **kwargs)
                return int(x)
            except:
                print('Ошибочка с данными')

        return call_int

    @staticmethod
    def to_str(func):
        @functools.wraps(func)
        def call_str(*args, **kwargs):
            print('Covert to int')
            try:
                x = func(*args, **kwargs)
                return str(x)
            except:
                print('Ошибочка с данными')
        return call_str

    @staticmethod
    def to_bool(func):
        @functools.wraps(func)
        def call_bool(*args, **kwargs):
            print('Convert to bool')
            try:
                x = func(*args, **kwargs)
                return bool(x)
            except:
                print('Ошибочка с данными')
        return call_bool

    @staticmethod
    def to_float(func):
        @functools.wraps(func)
        def call_float(*args, **kwargs):
            print('Convert to float')
            try:
                x = func(*args, *kwargs)
                return float(x)
            except:
                print('Ошибочка с данными')
        return call_float



@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True