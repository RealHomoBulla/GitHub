'''
Task 4
The math quiz program

"Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
'''

expression = 6*7
if input('What is the answer to this expression:\n6 * 7 = ').strip() == str(expression): print(f'That\'s right, {expression}!')
else: print('You don\'t know the Answer!')

