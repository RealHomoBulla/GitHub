"""
Task 2
Manipulate strings.

Save your first and last name as separate variables, then use string concatenation to add them together with a white space
in between and print a greeting.
"""

first_name = 'Andrew'
last_name = 'Shargorodskyi'

# Option 1, with string concatenation
print('Hello, ' + first_name + ' ' + last_name + '. \nHow are you?')

# or we can use 'F-string'

print(f'Hello, {first_name} {last_name}. \nHow are you?')
