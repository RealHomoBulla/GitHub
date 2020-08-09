'''Task 2. Extend Phonebook application

Functionality of Phonebook application:
 - Add new entries
 - Search by first name
 - Search by last name
 - Search by full name
 - Search by telephone number
 - Search by city or state
 - Delete a record for a given telephone number
 - Update a record for a given telephone number
 - An option to exit the program
The first argument to the application should be the name of the phonebook. Application should load JSON data,
if it is present in the folder with application, else raise an error. After the user exits,
all data should be saved to loaded JSON.
'''

import os, json, uuid
PHONEBOOK_FILE_NAME = 'pb.json'

# If JSON file was not found, some Default phonebook will be taken to introduce the App.
def get_phone_book(PHONEBOOK_FILE_NAME):
    try:
        with open(PHONEBOOK_FILE_NAME, 'r') as f:
            phonebook = json.load(f)
            print(f"\nSome Data was loaded from JSON file '{PHONEBOOK_FILE_NAME}'.")
            return phonebook
    except:
        print(f"\nThe JSON file '{PHONEBOOK_FILE_NAME}' was not found.\n\
Sample Database with Example Contacts was loaded to introduce you the functionality of this App.")
        phonebook = [ {'Name': 'Andrii', 'Surname': 'Shargorodskyi', 'Full Name': '', 'Country': 'Ukraine',
                          'City': 'Odessa','Phone': '0930423834', 'App_No': ''},
                    {'Name': 'Vasiliy', 'Surname': 'Pupkin', 'Full Name': '', 'Country': 'Ukraine',
                          'City': 'Kyiv', 'Phone': '0501013233', 'App_No': ''} ]
        return phonebook

# I made ID numbers 'App_No' to introduce person with a number. Also, you can search contact by his/her number.
def print_phonebook():
    for contact in phonebook:
        print(f"\n-----Contact #{contact['App_No']}-----")
        print_single_contact(contact)
    input('\nPress [Enter] to continue.')
# To print separate contacts another function is used.
def print_single_contact(contact):
    for k, v in contact.items():
        if k != 'App_No':
            print(f'{k} : {v}')

# 'Full Name' and 'App_No' are empty, because they are assigned automatically in the Main Function every iteration.
def add_new_contact():
    phonebook.append({
        'Name': input('\nInsert First Name: '),
        'Surname': input('Insert Last Name: '),
        'Full Name': '',
        'Country': input('Insert Country: '),
        'City': input('Insert City: '),
        'Phone': input('Insert Phone: '),
        'App_No': ''
    })
    print('\nNew Contact was added to your Contact List.')
    input('\nPress [Enter] to continue.')

# This function takes an argument 'action' because it can be used to Edit and to Remove Contact.
# It will make search by Full Name and return found contact for that specific action.
def choose_contact(action):
    contact_to_choose = ''
    while not quit_or_menu(contact_to_choose):
        contact_to_choose = input(f"\nWhich Contact would you like to {action}?\n\
Please enter the Full Name (Surname Name)\nFor example, 'Pupkin Vasiliy': ")
        for contact in phonebook:
            if contact['Full Name'].lower().replace(' ', '') == contact_to_choose.lower().replace(' ', ''):
                print(f"\nOkay, you are going to {action} Contact '{contact['Full Name']}'")
                print_single_contact(contact)
                input('\nPress [Enter] to continue.')
                return contact
        if contact_to_choose not in 'qm':
            print(f"Sorry, you don't seem to have '{contact_to_choose}' in your Contact List. Try Again.")

# To edit contact I use While-Loop to handle incorrect input and to ask again. To break the loop user
# may press M or Q to go to Main Menu or Quit.
def editing_contact(contact):
    info_to_edit = ''
    while not quit_or_menu(info_to_edit):
        info_to_edit = input('\nWhat would you like to Edit? \n"1" for Name, \n"2" for Surname, \
        \n"3" for Country, \n"4" for City,\n"5" for Phone"\nPlease Enter Number to choose (or [M/m] for Menu): ')
        if info_to_edit == '1':
            contact['Name'] = input('Enter new Name: ')
            print(f"Name was successfully changed to '{contact['Name']}'.")
        elif info_to_edit == '2':
            contact['Surname'] = input('Enter new Surname: ')
            print(f"Surname was successfully changed to '{contact['Surname']}'.")
        elif info_to_edit == '3':
            contact['Country'] = input('Enter new Country: ')
            print(f"Country was successfully changed to '{contact['Country']}'.")
        elif info_to_edit == '4':
            contact['City'] = input('Enter new City: ')
            print(f"City was successfully changed to '{contact['City']}'.")
        elif info_to_edit == '5':
            contact['Phone'] = input('Enter new Phone Number: ')
            print(f"Phone was successfully changed to '{contact['Phone']}'.")

# It will remove the contact by searching it with Full Name.
def remove_contact(contact):
    for i in range(len(phonebook)):
        if phonebook[i]['Full Name'] == contact['Full Name']:
            del phonebook[i]
            break

# Search is just showing us where the item was found. To edit it or delete, you have to go to the contact editor
# using the Main Menu.
def search_contact():
    part_to_search = ''
    found_items = []
    found_contacts = []
    while not quit_or_menu(part_to_search):
        i = 0
        part_to_search = input(f"\nWhat would you like to Search for?\nPlease enter any data like Name, City etc.: ")
        print(f"\nOkay, will try to find '{part_to_search}' in your Phonebook.")
        for contact in phonebook:
            for value in contact.values():
                if part_to_search.lower() in str(value).lower():
                    found_items.append(value)
                    print(f"I found '{value}' in contact '{contact['Full Name']}'.")
                    i += 1
        if i > 0:
            print(f'Search has found {i} items in total.')
        else:
            print('Sorry, your request was not successful.')

# This function saves the current Phonebook to a JSON file for future use when user Quits the App.
def store_phone_book():
    with open(PHONEBOOK_FILE_NAME, 'w') as f:
        json.dump(phonebook, f)

# This function is used to handle wrong input and to Make endless loop, allowing us to Quit or go to Main Menu.
def quit_or_menu(user_input):
    if user_input.lower().replace(' ', '') == 'q':
        print(f"\nAny changes will be saved to a file '{PHONEBOOK_FILE_NAME}' for future use.")
        print('Thank you for using our Contacts App!')
        store_phone_book()
        quit()
    elif user_input.lower().replace(' ', '') == 'm' or user_input.lower().replace(' ', '') == 'n':
        print('\nOkay, going back to Main Menu.')
        main_menu()
    else:
        return False

# This is the main body, which is navigated by numbers and letters and where some extra code executed.
def main_menu():
    menu_choice = ''
    while not quit_or_menu(menu_choice):
        number_counter = 0
        for contact in phonebook:
            number_counter += 1
            # Every iteration it re-assigns the numbers and Full Names, so that if anything was changed or if
            # any contact was removed, numbers were kept in correct sequence.
            contact['App_No'] = number_counter
            contact['Full Name'] = f"{contact['Surname']} {contact['Name']}"
        menu_choice = input('''\n1. Show Contacts List
2. Add New Contact
3. Edit Contact
4. Remove Contact
5. Search

Also, anywhere in the Program you can use: 
[M/m] - Main Menu
[Q/q] - Quit

Your action: ''')
        if menu_choice == '1':
            print_phonebook()
        elif menu_choice == '2':
            add_new_contact()
        elif menu_choice == '3':
            contact = choose_contact('Edit')
            editing_contact(contact)
        elif menu_choice == '4':
            contact = choose_contact('Remove')
            remove_contact(contact)
        elif menu_choice == '5':
            search_result = search_contact()


global phonebook
phonebook = get_phone_book(PHONEBOOK_FILE_NAME)
main_menu()
