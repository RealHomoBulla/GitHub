'''Task 4
Custom exception
Create your custom exception named `CustomException`, you can inherit from base Exception class,
but extend its functionality to log every error message to a file named `logs.txt`.
Tips: Use __init__ method to extend functionality for saving messages to file'''


print()
str_to_check = "There are so many niggers out there, waiting for our wallets."

class N_Word_Found_Exception(Exception):
    '''This exception is thrown when something which should be censored was said.'''
    def __init__(self, my_str):
        self.my_str = my_str
    def __str__(self):
        return f"N_Word_Found_Exception: N-Word was  found in the following line:\n\t'{self.my_str}'\n\
Shame on you, racist!"


try:
    if 'nigg' in str_to_check:
        raise  N_Word_Found_Exception(str_to_check)
    else: print('Okay, you passed the censorship.')
except N_Word_Found_Exception as exception:
    print('Watch your language! You should not talk like that!')
    with open('error_log.txt', 'a') as f:
        f.write('\n'+str(exception))

