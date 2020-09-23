'''
Task 5
def sum_of_digits(digit_string: str) -> int:
     -> sum_of_digits('26') == 8
    True
     -> sum_of_digits('test')
    ValueError("input string must be digit string")
'''


def sum_of_num(num: str) -> int:
    if len(num) == 1:
        return int(num[0])
    return int(num[0]) + int(sum_of_num(num[1:]))

print(sum_of_num('2428'))
print(sum_of_num('2'))
print(sum_of_num('228'))