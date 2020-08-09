'''Task 2
Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).'''

def strange_function():
    while True:
        try:
            a, b = input('Please give me 2 numbers (a and b), separated by comma: ').replace(' ', '').split(',')
            a = int(a)
            b = int(b)
            return f'"a" squared and divided by "0" equals to: {a**2/b}'
        except ZeroDivisionError:
            print('You are not supposed to divide by Zero. Try again: ')
            continue
        except ValueError:
            print('Please enter TWO valid numbers. Try again: ')
            continue
        except:
            print('Something really unexpected happened. Try again: ')
            continue


x = strange_function()
print(x)