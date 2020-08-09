        """
Task 2
The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""

while True:
    phone_number = input('Please enter your Mobile: ')
    if len(phone_number) == 10 and phone_number.isdigit() == True:
        print(f'You have entered a valid phone number: {phone_number}')
        break
    else:
        print('Your input seems incorrect. Please try to enter 10-digit number: ')
        continuelen