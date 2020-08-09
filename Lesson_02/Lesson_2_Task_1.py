"""
Task 1
The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:
     “Good day <name>! <day> is a perfect day to learn some python.”
Note that <name> and <day> are predefined variables in source code.
An additional bonus will be to use different string formatting methods for constructing result string.
"""

user_name = 'Andrew'
current_day = 'Monday'

# Method 1
print(f'Good day {user_name}! {current_day} is a perfect day to learn some python.')

# Method 2
print('Good day '+ user_name + '! ' + current_day + ' is a perfect day to learn some python.')

# Method 3
print('Good day {0}! {1} is a perfect day to learn some python.'.format(user_name, current_day))

# Method 4
print('Good day %s! %s is a perfect day to learn some python.' % (user_name, current_day))

# Method 5 
string = 'Good day {}! {} is a perfect day to learn some python.'
print(string.format(user_name, current_day))