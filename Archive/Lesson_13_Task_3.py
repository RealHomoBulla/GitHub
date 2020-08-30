'''Task 3
Write a function called `choose_func` which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one'''

# This function will be doubling every number in the list.
def double(some_list):
    result = []
    for num in some_list:
        result.append(num * 2)
    return result

# This function will be tripling every number in the list.
def triple(some_list):
    result = []
    for num in some_list:
        result.append(num * 3)
    return result

# Just to check if it works.
print(double([1, 2, 3, 4, 5]))
print(triple([1, 2, 3, 4, 5]))
print()


def choose_func(list_of_nums, func_1, func_2):

    # This function will check, if ALL the numbers in the list are positive. Otherwise it returns False.
    def check_the_list():
        for num in list_of_nums:
            # If any number is negative, func_2 will be executed (in our case, number will triple).
            if num < 1:
                return func_2(list_of_nums)
        # If all numbers are positive, func_1 will be executed (in our case, number will double).
        return func_1(list_of_nums)
    return check_the_list()

# Checking - numbers should be doubled.
print(choose_func([1, 2, 3, 4, 5], double, triple))
# Checking - numbers should be tripled.
print(choose_func([1, -2, 3, 4, 5], double, triple))