'''
Task 3
Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5,
and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
'''

list_1_to_100 = list(range(0, 100))
list_special_numbers = []
i = 0

while i < len(list_1_to_100):
    if list_1_to_100[i] % 7 == 0 and list_1_to_100[i] % 5 != 0:
        list_special_numbers.append(list_1_to_100[i])
    i += 1


print(f'\nThe following numbers in the range from 1 to 100 are divisible by 7 but not a multiple of 5:\n{list_special_numbers}')







