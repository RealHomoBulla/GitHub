from functools import wraps

def logit(logfile='program_execution.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            log_string = f'{func.__name__} was called.'
            print(log_string)
            with open(logfile, 'a') as f:
                f.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_func
    return logging_decorator

# @logit()
# def myfunc1():
#     pass
#
#
# myfunc1()

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()