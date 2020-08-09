'''
Task 1
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
'''

from random import randint
from time import sleep

random_list = []
i = 0

while i != 10:
    random_list.append(randint(1, 10))
    i += 1

print('\nGenerating a list with ten random numbers from 1 to 10. Please stand-by.')
for r in range(3):
    print('...')
    sleep(1)
print(f'Okay, we\'ve got a list:\n{random_list}')
print(f'The largest number that was generated is {max(random_list)}.')