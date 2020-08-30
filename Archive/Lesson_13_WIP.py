import datetime, json

PHONEBOOK_FILE_NAME = 'pb.json'

class Human:
    def  __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def __eq__(self, other):
       return (self.name, self.last_name) == (other.name, other.last_name)

    def __str__(self):
        return f'''
Name:               {self.name} 
Last Name:          {self.last_name}
Mobile:             {self.get_phone()}'''

    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def create_dict(self):
        return {'Name': self.name,
                'Last Name': self.last_name,
                'Phone': self.phone,
                'isColleague': False}
    def read_data(self, data):
        self.name = data['Name']
        self.last_name = data['Last Name']
        self.phone = data['Phone']


class Colleague(Human):
    def __init__(self, name, last_name, phone, work_phone):
        super().__init__(name, last_name, phone)
        self.work_phone = work_phone

    def get_phone(self):
        if 10 < datetime.datetime.now().hour < 18:
            return self.work_phone
        return super().get_phone()
    def create_dict(self):
        return {'Name': self.name,
                'Last Name': self.last_name,
                'Phone': self.phone,
                'Work Phone': self.work_phone,
                'isColleague': True}
    def read_data(self, data):
        self.name = data['Name']
        self.last_name = data['Last Name']
        self.phone = data['Phone']
        self.work_phone = data['Work Phone']


class Phonebook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.contacts = []
        try:
            print(f"\nThe JSON file '{file_name}' was loaded.")
            with open(file_name, 'r') as f:
                temp = json.load(f)
        except:
            print(f"\nThe JSON file '{file_name}' was not found.\
Sample Database with Example Contacts was loaded to introduce you the functionality of this App.\n")
            with open(file_name, 'w') as f:
                temp = [{'Name': 'Vasiliy', 'Last Name': 'Pupkin', 'Phone': '0501013233', 'isColleague': False},
                        {'Name': 'Vasiliy', 'Last Name': 'Pupkin', 'Phone': '0501013233', 'work_phone': '234023502350',
                         'isColleague': True}]
                json.dump(temp, f)
        finally:
            for i in temp:
                new_person = self.return_person(i['Name'], i['Last Name'], i['Phone'], i.get('work_phone', ''), i.get('isColleague'))
                self.add_person(new_person)

    def __len__(self):
        return len(self.contacts)

    def store(self):
        list_to_save = [c.create_dict() for c in self.contacts]
        print(list_to_save)
        try:
            with open(self.file_name, 'w') as f:
                json.dump(list_to_save, f)
        except:
            print('Can\'t save the file for some reason.')

    def return_person(self, name, last_name, phone, work_phone='', isColleague=True):
        if isColleague:
            return Colleague(name, last_name, phone, work_phone)
        return Human(name, last_name, phone)

    def add_person(self, person):
        if person not in self.contacts:
            self.contacts.append(person)

    def remove_person(self, person):
        if person in self.contacts:
            self.contacts.remove(person)

    def print_phonebook(self):
        for contact in self.contacts:
            print(contact)

if __name__ == '__main__':
    phonebook_1 = Phonebook(PHONEBOOK_FILE_NAME)
    # phonebook_1.print_phonebook()
    person_1 = phonebook_1.return_person('Petr', 'Petrov', '+380930423834', isColleague=False)
    phonebook_1.add_person(person_1)
    phonebook_1.remove_person(person_1)
    phonebook_1.print_phonebook()
    print(f"\nThe length of phonebook '{phonebook_1.file_name}' is {len(phonebook_1)}.")
















    # phonebook_1.add_person(person_1)

    # phonebook_1.remove_person(person_1)
    # phonebook_1.print_phonebook()











    # a =  person_1.create_dict()
    # print(a)
    # a['Name'] = 'Nikodim'
    # person_1.read_data(a)
    # print(person_1)
    # print(phonebook_1.contacts)
    # phonebook_1.store()

    #
    # person_2 = phonebook_1.return_person('Perya', 'Petrov', '+380930424593', work_phone='+34354350', isColleague=True)

    # phonebook_1.print_phonebook()

