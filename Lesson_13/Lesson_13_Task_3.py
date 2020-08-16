'''Task 3
Write a function called `choose_func` which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one'''


# I decided to give it 2 standard functions, but make it possible to give 2 other functions from outside.
# So, if you pass it only a list, and list is all positive, it will double every number in the list;
# If any number there is negative, it will triple the numbers;
# And if you pass with your 2 functions, it will execute these 2 functions.
def choose_func(list_of_nums, func_1='double', func_2='triple'):

    # This function will be doubling every number in the list.
    def double():
        result = []
        for num in list_of_nums:
            result.append(num * 2)
        return result

    # This function will be tripling every number in the list.
    def triple():
        result = []
        for num in list_of_nums:
            result.append(num * 3)
        return result

    func_dict = {
        'double': double,
        'triple': triple
    }

    # This function will check, if ALL the numbers in the list are positive. And depending on that, it returns
    # one function or the other.
    def check_the_list():
        for num in list_of_nums:
            # If any number is negative, func_2 will be executed (in our case, number will triple).
            if num < 1:
                # This line checks, if extra arguments with function was given. If so, it  will execute the function
                # that was given. Otherwise it will execute the standard func_2, which is 'triple'.
                if func_2 != 'triple': return func_2(list_of_nums)
                return func_dict['triple']()
        # If all numbers are positive, func_1 will be executed (in our case, number will double).
        if func_1 != 'double': return func_1(list_of_nums)
        return func_dict['double']()
    return check_the_list()



# Now I will test it without extra functions in arguments, just with list.
positive_list = [1, 2, 3, 4, 5]
negative_list = [1, 2, 3, -4, 5]

# Checking - numbers should be doubled.
print(choose_func(positive_list))

# Checking - numbers should be tripled.
print(choose_func(negative_list))



# Now I want to define some functions outside and test with them.
def divide_by_2(list_of_nums):
    result = []
    for num in list_of_nums:
        result.append(num / 2)
    return result

def divide_by_3(list_of_nums):
    result = []
    for num in list_of_nums:
        result.append(num / 3)
    return result

# This will execute the 'divide_by_2' function (list is positive)
print(choose_func(positive_list, divide_by_2, divide_by_3))

# This will execute the 'divide_by_3' function (list is negative)
print(choose_func(negative_list, divide_by_2, divide_by_3))