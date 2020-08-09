"""
Task 3
The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
if your input is “Anton” and the stored name is “anton”, it should return True.
"""

# Stored name
name = 'andrew'

def name_check():
    input_name = input('What is your name? ')
    if input_name.lower().strip() == name:    # Here it will make it lower-case and remove accidental spaces.
        print('That is you!')
        return True
    else:
        print('It is someone else')
        return False

name_check()