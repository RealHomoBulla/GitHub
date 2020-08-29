'''Task 2
Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function'''

def in_range(start=0, stop=0, step=1): # я переписал как у тебя все три опциональные но по ТЗ только шаг опционален. То есть старт и енд всегда должны быть
    start, stop = (min(start, stop), max(start, stop)) if step>0 else (max(start, stop), min(start, stop))
    while ((start < stop) if step>0  else ( start > stop)):
        yield start
        start += step

# Works with only one argument.
for i in in_range(10):
    print(i)

print('')

# Works with two arguments.
for i in in_range(1, 10):
    print(i)

print('')

# Works with step argument, and with negative step as well.
for i in in_range(100, -10, -10):
    print(i)

# Gives an error if there is no arguments, or if there is more than 3 arguments, same as original "range" fucntion.
# for i in in_range():
#     print(i)

# for i in in_range(1, 10, 1, 1):
#     print(i)

