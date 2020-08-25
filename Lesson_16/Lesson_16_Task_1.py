'''Task 1
Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
`iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function'''

def with_index(iterable, start=0):
    for item in iterable:
        yield (start, item)
        start += 1

# List to  test our function.
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

for i in with_index(seasons):
    print(i)

print('\n')

for i, value in with_index(seasons, 1):
    print(i, value)

print('\n')

print(list(with_index(seasons, 1)))


# Dictionary to test our function.
seasons_dict = {'Spring is': 'Awesome', 'Summer is': 'Good', 'Fall is': 'Okay', 'Winter is': 'The Best'}


for i in with_index(seasons_dict, 1):
    print(i)

print('\n')

for i, (k, v) in with_index(seasons_dict.items(), 1):
    print(i, k, v)

for i in range(-10):
    print(i)