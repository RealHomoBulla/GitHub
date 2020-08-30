def full_name(first, last):
    return f'{first.title()} {last.title()}'

def square_nums(lst):
    res = []
    for i in lst:
        res.append(i ** 2)
    return res

if __name__ == '__main__':
    print('This code will not be executed if module is imported, but will be executed if you run this module.')