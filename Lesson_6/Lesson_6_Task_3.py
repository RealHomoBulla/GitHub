''' Task 3
List comprehension exercise:
Use a list comprehension to make a list containing tuples (i, j),
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.'''

# Method 1 is more simple, but it's not saving these Tuples for further use.
print('\nPrinting a List using single-line list comprehension (list is not saved as a variable):')
print([tuple([i for i in range(1, 11)]), tuple([j ** 2 for j in range(1, 11)])])


# Method 2 is better if you need to use this Tuples or List later.
i = tuple([i for i in range(1, 11)])
j = tuple([j ** 2 for j in range(1, 11)])
common_list = [i, j]

print('\nYou can access list now and it is saved as variable:')
print(common_list)
print('\nTuples are saved separately as well:')
print(i)
print(j)