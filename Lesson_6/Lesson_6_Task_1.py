'''Task 1
Make a program that has some sentence (a string) on input and returns a dict containing
all unique words as keys and the number of occurrences as values.'''

from re import sub
from collections import OrderedDict

print('\nI can separate each word and count how many times it occurred in the text for you.\
       \nMost frequent words will be higher in the list.')
test_string = input('Please, enter some string:\n')
test_dict = dict()

# I made a function, so that Dict and Str remain undamaged and could be re-used.
def word_counter(sentence, dictionary):
    # Make it lowercase and separate the words.
    sentence = sentence.lower().split(' ')
    for word in sentence:
            # Need to remove possible spaces, punctuation marks etc.
            word = sub(r'\W+', '', word)
            # Check whether the word is already in dictionary.
            if word in dictionary:
                # Increment counter of word by 1.
                dictionary[word] += 1
            else:
                # Add the word to dictionary with count 1 (first occurrence).
                dictionary[word] = 1

    # I had a bug with double-spaces. They would create empty Key, so it should be removed.
    if '' in dictionary:
        del dictionary['']

    # Sorting words by frequency of occurrence.
    dictionary = OrderedDict(sorted(dictionary.items(), key=lambda t: t[1], reverse=True))
    # Printing the Key-Value pair.
    for key, value in list(dictionary.items()):
        print(f'"{key}": {value}')

word_counter(test_string, test_dict)

