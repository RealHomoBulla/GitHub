'''Task 1
Imports practice
Make a directory with 2 modules; make a function in one of them;
then import this function in the other module and use that in your script of choice.'''

import some_module as m

if __name__ == '__main__':
    print(m.square_nums([1, 2, 3, 4]))
    print(m.full_name('Carl', 'Johnson'))

    x = 10