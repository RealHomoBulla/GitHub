'''
Task 2
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
'''

from random import randint

random_list_1 = []
random_list_2 = []
final_set = set()
i = 0

while i != 10:
    random_list_1.append(randint(1, 10))
    random_list_2.append(randint(1, 10))
    i += 1
print(f'\nOkay, we\'ve got two lists with ten random numbers (each) from 1 to 10:\n{random_list_1}\n{random_list_2}')

final_set = list(final_set.union(random_list_1, random_list_2))
print(f'\nNow we can unite them, taking common integers, and removing duplicates:\n{final_set}')
