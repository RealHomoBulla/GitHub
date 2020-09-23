'''
Task 4
def reverse(input_str: str) -> str:
    Function returns reversed input string
     -> reverse("hello") == "olleh"
    True
     -> reverse("o") == "o"
    True
'''


def reverse(s: str) -> str:
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("hello") == "olleh")
print(reverse("o") == "o")