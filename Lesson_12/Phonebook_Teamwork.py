'''класс Человек
- имя
- фамилия
- телефон
== установить новый телефон
== получить текущий телефон
класс Коллега тоже Человек
- рабочий телефон
== установить рабочий телефон
Телефонная книга класс
Конструктор принимает имя файла, деструктор — сохраняет список контактов на диск.
== добавить “запись” (перед добавлением проверяет что такой еще нет. Если есть то заменяет ее. Записи равны если имя и фамилия равна )
== длинна экземпляра = количеству записей в книге (дюндер магические)
== метод получить запись (создает или Человека или Коллегу на вход принимает имя фамилию и так далее.)
== поиск значению атрибута (принимает поле и его значение first_name “атя” getattr )
== удаление переданного обьекта (чтоб удалить какую то запись создаем запись с именем и фамилией которую надо удалить и передаем этому методу)
== добавить круговое листание'''

import datetime
import json
import os

PHONE_BOOK_NAME = 'phonebook_lesson.json'


class Human:

    def __init__(self, name, second_name, phone):
        self.name = name
        self.second_name = second_name
        self.phone = phone

    # Метод для сравнения вида '=='.
    def __eq__(self, other):
        return (self.name, self.second_name) == (other.name, other.second_name)

    # Строковое отображение экземпляра класса.
    def __str__(self):
        return (f'''
Имя:              {self.name}
Фамилия:          {self.second_name}
Моб. номер:       {self.get_phone()}''')

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    # Создает словарь из объекта. Используется для записи в JSON и для поиска (поиск по items).
    def create_dict(self):
        return {
            'Name': self.name,
            'Last Name': self.second_name,
            'Phone': self.phone,
            'Is college': False
        }

    # Считывает словарь и обновляет аттрибуты класса.
    def fill_data(self, data):
        self.name = data['Name']
        self.second_name = data['Last Name']
        self.phone = data['Phone']


class College(Human):

    def __init__(self, name, second_name, phone, work_phone):
        super().__init__(name, second_name, phone)
        self.work_phone = work_phone

    # Возвращает номер телефона (личный или рабочий) в зависимости от времени суток.
    def get_phone(self):
        if 10 <= datetime.datetime.now().hour < 18:
            return self.work_phone
        return super().get_phone()

    # Создает словарь из объекта. Используется для записи в JSON и для поиска (поиск по items). Отличается наличием 'Work Phone'.
    def create_dict(self):
        return {
            'Name': self.name,
            'Last Name': self.second_name,
            'Phone': self.phone,
            'Work Phone': self.work_phone,
            'Is college': True
        }

    # Считывает словарь и обновляет аттрибуты класса. Отличается наличием 'Work Phone'.
    def fill_data(self, data):
        self.name = data['Name']
        self.second_name = data['Last Name']
        self.phone = data['Phone']
        self.work_phone = data['Work phone']


class PhoneBook:

    def __init__(self, name_file):
        self.name_file = name_file
        self.list_contacts_obj = []
        self.chosen_contact = 0
        # Вызывается метод для проверки наличия Базы Данных. Если не найдена, внутри него вызовется метод создания Демо-базы.
        self.open_db()

    def __len__(self):
        length = len(self.list_contacts_obj)
        print(f'\nВ контактной книге найдено: {length} контакта.')
        return length

    # Создает Демо-базу из 4х вымышленных контактов для демонстрации работы программы.
    def create_demo(self):
        demo_db = [
            {
                'Name': 'Vasiliy',
                'Last Name': 'Pupkin',
                'Phone': '0501012333',
                'Is college': False
            },
            {
                'Name': 'Jonathan',
                'Last Name': 'Blame',
                'Phone': '0123654987',
                'Work phone': '234023502350',
                'Is college': True
            },
            {
                'Name': 'Ithan',
                'Last Name': 'Lamerson',
                'Phone': '0234567890',
                'Is college': False
            },
            {
                'Name': 'Liy',
                'Last Name': 'Pipkin',
                'Phone': '050123502350',
                'Work phone': '4923592340',
                'Is college': True
            }]
        # Добавляет все контакты в главный Список Контактов
        for i in demo_db:
            self.list_contacts_obj.append(i)
        # Записывает Список Контактов в JSON для последующей работы.
        with open(self.name_file, 'w') as f_obj:
            json.dump(self.list_contacts_obj, f_obj)

    # При запуске программы проверяет наличие Базы Данных.
    def open_db(self):
        if not os.path.isfile(f'./{PHONE_BOOK_NAME}'):
            print(f'JSON file {PHONE_BOOK_NAME} not found.')
            # База данных не найдена, создается Демо
            self.create_demo()
        elif os.path.isfile(f'./{PHONE_BOOK_NAME}'):
            with open(self.name_file, 'r') as f_obj:
                # Если найдена, считывает из файла и создает объекты контактов.
                temp = json.load(f_obj)
                try:
                    for contact in temp:
                        new_person = self.return_person(
                            contact['Name'], contact['Last Name'],
                            contact['Phone'], contact.get('Work phone', ''),
                            contact.get('Is college'))
                        self.add_person(new_person)
                except KeyError:
                    # Если не выходит считать объекты контактов, создает опять же демобазу
                    print('Ошибка с ключом. Демобаза будет создана.')
                    self.create_demo()
                except:
                    print('Что-то пошло совсем не так.')
                print(f'\nJSON file "{PHONE_BOOK_NAME}" was loaded\n')

    # Сохраняет книгу в JSON
    def save(self):
        list_to_write = [x.create_dict() for x in self.list_contacts_obj]
        try:
            with open(self.name_file, 'w') as f_obj:
                json.dump(list_to_write, f_obj)
        except:
            print('Не получилось сохранить файл')

    # Создает объект с переданными параметрами
    def return_person(self,
                      name,
                      second_name,
                      phone,
                      work_phone='',
                      is_college=True):
        if is_college:
            return College(name, second_name, phone, work_phone)
        else:
            return Human(name, second_name, phone)

    # Проверяет, существует ли добавляемый объект. Если не существует, успешно его добавляет.
    # Может вызываться из меню для добавления имени и данных вручную.
    def add_person(self, contact=None):
        if not contact:
            user_choice = ''
            print('\nYou are going to add a person.')
            name = input('Name: ')
            second_name = input('Second Name: ')
            phone = input('Phone: ')
            print('Is it your colleague?')
            while user_choice.lower() != 'y' or user_choice.lower() != 'n':
                user_choice = input('[Y/N]: ')
                if user_choice.lower() == 'y':
                    is_college = True
                    work_phone = input('Work Phone: ')
                    break
                elif user_choice.lower() == 'n':
                    is_college = False
                    work_phone = ''
                    break
            contact = self.return_person(name, second_name, phone, work_phone, is_college)
        if contact not in self.list_contacts_obj:
            self.list_contacts_obj.append(contact)

    # Метод для редактиирования данных контакта.
    def edit_contact(self, contact=None):
        if not contact:
            print('\nOkay. You are going to edit some contact.')
            contact = self.search_choose_one_contact()

        if contact in self.list_contacts_obj:
            info_to_edit = ''
            while not quit_or_menu(info_to_edit):
                info_to_edit = input('\nWhat would you like to Edit? \n"1" for Name, \n"2" for Surname, \
                        \n"3" for Phone, \n"4" to choose is it Colleague or not.\nPlease Enter Number to choose (or [M/m] for Menu): ')
                if info_to_edit == '1':
                    contact.name = input('Name: ')
                    print(f"Name was successfully changed to '{contact.name}'.")
                elif info_to_edit == '2':
                    contact.second_name = input('Second Name: ')
                    print(f"Surname was successfully changed to '{contact.second_name}'.")
                elif info_to_edit == '3':
                    contact.second_name = input('Phone: ')
                    print(f"Phone was successfully changed to '{contact.phone}'.")
                elif info_to_edit == '4':
                    user_choice = ''
                    print('Is it your colleague?')
                    while user_choice.lower() != 'y' or user_choice.lower() != 'n':
                        user_choice = input('[Y/N]: ')
                        if user_choice.lower() == 'y':
                            contact.is_college = True
                            contact.work_phone = input('Work Phone: ')
                            break
                        elif user_choice.lower() == 'n':
                            contact.is_college = False
                            contact.work_phone = ''
                            break

    # Удаляет контакт по имени, если объект не передан командой
    def delete_contact(self, contact=None):
        if not contact:
            print('\nOkay. You are going to delete some contact.')
            contact = self.search_choose_one_contact()
        if contact in self.list_contacts_obj:
            print(f'\nYour contact "{contact.name} {contact.second_name}" was successfully deleted. ')
            self.list_contacts_obj.remove(contact)


    # Печатает всю телефонную книгу + количество контактов в ней
    def print_phonebook(self):
        len(phone_book_1)
        for x in self.list_contacts_obj:
            print(x)

    # Ищет совпадения во всех графах контакта (по номерам, именам и тд, везде)
    def search_contact(self, search_line = ''):
        if not search_line:
            search_line = input('\nВведите искомый элемент: ')
        temp_list = []
        for contact in self.list_contacts_obj:
            contact_dict = contact.create_dict()
            if search_line.lower() in str(contact_dict.items()).lower():
                temp_list.append(contact)
        if len(temp_list) >= 1:
            print(f'\nHere is what was found on your search request: ')
            for n in temp_list:
                print(n)
        else:
            print('\nSeems like nothing was found, try again!')
        return temp_list

    # Дает выбрать один конкретный контакт, но нужно написать имя и фамилию в точности
    def search_choose_one_contact(self):
        user_choice = input('\nEnter the full name of chosen contact (Name Surname): ')
        for contact in self.list_contacts_obj:
            if str(f'{contact.name} {contact.second_name}') == user_choice:
                return contact
            continue

    # Показывает контакты в режиме листания, как на старом кнопочном телефоне.
    def showing_contact(self):
        user_choice = ''
        print('\nEnter [n] to see next contact, [p] to see previous, [m] to go to Main Menu.')
        while user_choice.lower() != 'm':
            print(self.current_contact())
            user_choice = input('\n[n]/[p]/[m]: ')
            if user_choice.lower() == 'n':
                self.next_contact()
            elif user_choice.lower() == 'p':
                self.prev_contact()

    def current_contact(self):
        return self.list_contacts_obj[self.chosen_contact]

    def next_contact(self):
        self.chosen_contact += 1
        if self.chosen_contact >= len(self.list_contacts_obj):
            self.chosen_contact = 0
        return self.list_contacts_obj[self.chosen_contact]

    def prev_contact(self):
        self.chosen_contact -= 1
        if self.chosen_contact < 0:
            self.chosen_contact = len(self.list_contacts_obj) - 1
        return self.list_contacts_obj[self.chosen_contact]

if __name__ == '__main__':

    # Initialize the phonebook (from file)
    phone_book_1 = PhoneBook(PHONE_BOOK_NAME)

    def demonstration(phone_book_1):

        # Print the Phonebook. Also, test inside the __len__ dunder method. Works fine
        phone_book_1.print_phonebook()

        # Adding the person works as well.
        person_1 = phone_book_1.return_person(
            'Ivan',
            'Jefferson',
            '0951234567',
            is_college=False,
            work_phone='789456')
        phone_book_1.add_person(person_1)
        # Also we can print separate person just fine.
        print('\nNow separate contact will be printed!\n', person_1)

        # Check if he added to phonebook and if __len__ changes:
        phone_book_1.print_phonebook()

        # Delete this person:
        phone_book_1.delete_contact(person_1)
        # Also, delete works without argumant, searching for a contact.
        phone_book_1.delete_contact()

        # Check again if delete function works:
        phone_book_1.print_phonebook()

        phone_book_1.search_contact()

    # !!! YOU CAN  COMMENT OUT THIS LINE TO TEST HOW ITS USED WITHOUT MENU !!!
    # demonstration(phone_book_1)


    # Функция для возврата в главное меню, для выхода с сохранением
    def quit_or_menu(user_input):
        if user_input.lower().replace(' ', '') == 'q':
            print(f"\nAny changes will be saved to a file '{PHONE_BOOK_NAME}' for future use.")
            print('Thank you for using our Contacts App!')
            phone_book_1.save()
            quit()
        elif user_input.lower().replace(' ', '') == 'm':
            print('\nOkay, going back to Main Menu.')
            menu()
        else:
            return False

    # Тело главного меню, циклично работает, пока пользователь не решит выйти.
    # Каждый цикл книга пересохраняется на всякий случай.
    def menu():
        menu_choice = ''
        while not quit_or_menu(menu_choice):
            phone_book_1.save()
            menu_choice = input('''\n1. Show All Contacts
2. Single Contact View
3. Add Contact
4. Edit Contact
5. Remove Contact
6. Search

Also, anywhere in the Program you can use: 
[M/m] - Main Menu
[Q/q] - Quit

Your action: ''')
            if menu_choice == '1':
                phone_book_1.print_phonebook()
            elif menu_choice == '2':
                phone_book_1.showing_contact()
            elif menu_choice == '3':
                phone_book_1.add_person()
            elif menu_choice == '4':
                try:
                    phone_book_1.edit_contact()
                except:
                    print('\nSomething went wrong. You will continue from Main Menu.\nPlease be careful with input!')
                    menu()
            elif menu_choice == '5':
                try:
                    phone_book_1.delete_contact()
                except:
                    print('\nSomething went wrong. You will continue from Main Menu.\nPlease be careful with input!')
                    menu()
            elif menu_choice == '6':
                phone_book_1.search_contact()

    menu()