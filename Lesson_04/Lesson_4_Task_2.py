'''
Task 2
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”
'''

name = input('What is your name?\n').capitalize()
while True:
    age = input('How old are you?\n')
    # Now I want to make sure that user input will be a positive number
    if age.isdigit() and int(age) > 0:
        age = int(age)
        break
    else:
        print('Please, check again.')
        continue

print(f'Hello, {name}, on your next birthday you\'ll be {age+1} years old!')
