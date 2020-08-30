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

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def create_dict(self):
        return {
            'Name': self.name,
            'Last Name': self.second_name,
            'Phone': self.phone,
            'Is college': False
        }

    def fill_data(self, data):
        self.name = data['Name']
        self.second_name = data['Last Name']
        self.phone = data['Phone']

    def __eq__(self, other):
        return (self.name, self.second_name) == (other.name, other.second_name)

    def __str__(self):
        return (f'''
Имя:              {self.name}
Фамилия:          {self.second_name}
Моб. номер:       {self.get_phone()}''')


class College(Human):
    def __init__(self, name, second_name, phone, work_phone):
        super().__init__(name, second_name, phone)
        self.work_phone = work_phone

    def get_phone(self):
        if 10 <= datetime.datetime.now().hour < 18:
            return self.work_phone
        return super().get_phone()

    def create_dict(self):
        return {
            'Name': self.name,
            'Last Name': self.second_name,
            'Phone': self.phone,
            'Work phone': self.work_phone,
            'Is college': True
        }

    def fill_data(self, data):
        self.name = data['Name']
        self.second_name = data['Last Name']
        self.phone = data['Phone']
        self.work_phone = data['Work phone']


class PhoneBook:
    def __init__(self, name_file):
        self.name_file = name_file
        self.list_contacts_obj = []
        self.open_db()

    def create_demo(self):
        demo_db = [{
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
        for i in demo_db:
            self.list_contacts_obj.append(i)
        with open(self.name_file, 'w') as f_obj:
            json.dump(self.list_contacts_obj, f_obj)

    def open_db(self):
        if not os.path.isfile(f'./{PHONE_BOOK_NAME}'):
            print(f'JSON file {PHONE_BOOK_NAME} not found.')
            self.create_demo()
        elif os.path.isfile(f'./{PHONE_BOOK_NAME}'):
            with open(self.name_file, 'r') as f_obj:
                temp = json.load(f_obj)
                try:
                    for contact in temp:
                        new_person = self.return_person(
                            contact['Name'], contact['Last Name'],
                            contact['Phone'], contact.get('Work phone', ''),
                            contact.get('Is college'))
                        self.add_person(new_person)
                    print(f'{temp}\n')
                except KeyError:
                    print('Ошибка с ключом')
                except:
                    raise
                print(f'JSON file {PHONE_BOOK_NAME} was loaded\n')

    def save(self):
        list_to_write = [x.create_dict() for x in self.list_contacts_obj]
        try:
            with open(self.name_file, 'w') as f_obj:
                json.dump(list_to_write, f_obj)
        except:
            print('Не получилось сохранить файл')

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

    def add_person(self, contact):
        if contact not in self.list_contacts_obj:
            self.list_contacts_obj.append(contact)

    # TODO: Можно добавить подтвреждение/вопрос про удаление
    def delete_contact(self, contact):
        if contact in self.list_contacts_obj:
            self.list_contacts_obj.remove(contact)

    def print_phonebook(self):
        for x in self.list_contacts_obj:
            print(x)

    # def print_contact(self)

    def search_contact(self):
        search_line = input('Введите искомый элемент: ')
        temp_list = []
        for contact in self.list_contacts_obj:
            contact_dict = contact.create_dict()
            if search_line in str(contact_dict.items()):
                temp_list.append(contact)
        print('\nHere is what i found: ')
        for n in temp_list:
            print(n)

        # TODO: make contact choice to return some contact


def print_single_contact(contact):
    for k, v in contact.items():
        if k != 'App_No':
            print(f'{k} : {v}')


if __name__ == '__main__':
    phone_book_1 = PhoneBook(PHONE_BOOK_NAME)
    person_1 = phone_book_1.return_person(
        'Ivan',
        'Jefferson',
        '0951234567',
        is_college=False,
        work_phone='789456')

    # phone_book_1.add_person(person_1)

    # print(len(phone_book_1))
    # x = phone_book_1.search_contact()
    # print(x)

    # print(new_person.phone)
    # a = person_1.create_dict()
    # phone_book_1.print_phonebook()
    # phone_book_1.search_contact()

    # print(phone_book_1.list_contacts_obj[1].phone)

    # phone_book_1.delete_contact(person_1)

    # print(a)
    # a['Name'] = 'Nikodim'
    # person_1.fill_data(a)
    # print(person_1)
    # phone_book_1.add_person(person_1)
    # person_2 = phone_book_1.return_person('Jo', 'Stevenson', '05612645', is_college=True, work_phone='0123456')
    # phone_book_1.add_person(person_2)
    # phone_book_1.print_phonebook()
    # phone_book_1.save()

# TODO:
# Test work/home phone by time
# Make destructor for saving file.
# Make __len__ for PhoneBook class.
# Make delete function with search
# Cycle listing from beginning to end


# def found_chk(pb_rec, sample):
#     try:
#         rec_str = ''
#         for i in pb_rec.values():
#             rec_str += "~~|~~" + str(i)
#         return sample.lower() in rec_str.lower()
#     except:
#         return False


# class Person:
#     age = 23
#     name = "Adam"

# person = Person()

# when default value is provided
# print('The sex is:', getattr(person, 'sex', 'Male'))

# when no default value is provided
# print('The sex is:', getattr(person, 'sex'))


# print(phone_book_1.list_contacts_obj[1].phone)