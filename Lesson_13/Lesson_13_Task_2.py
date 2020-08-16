# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def make_multiplier(multiplier):
    def mul_func(num):
        return num * multiplier
    return mul_func

mul_10 = make_multiplier(10)

print(mul_10(30))
