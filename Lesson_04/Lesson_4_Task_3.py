'''
Task 3
Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine
characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
'''

from random import shuffle

user_string = input('Please, type in something: \n')

# I found random.shuffle and it's very useful in this case
def string_shuffle(string):
    # String is immutable, so we need to make a list, lists are mutable
    letters = list(string)
    shuffle(letters)
    # We return the word with letters joined one by one from the list
    return ''.join(letters)

# To make it 5 times, the best way is to use "For-Loop"
for i in range(5):
    print(string_shuffle(user_string))



#
# import random
#
# word = input("Please enter a word: ")
# s = 0
# while s != 5:
#     print(''.join(random.sample(word, len(word))))
#     s += 1
# print(word)