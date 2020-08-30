

#
# class People:
#     MAX_PEOPLE_AGE = 200
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.office = ''
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if type(value) is int:
#             if self.__age < value < People.MAX_PEOPLE_AGE:
#                 self.__age = value
#             else:
#                 print(f'Not more than {People.MAX_PEOPLE_AGE}')
#         else:
#             print('Wrong type. Integers only.')
#
#     @age.deleter
#     def age(self):
#         pass
#
#     @property
#     def __posada_file(self):
#         return f'posads_{self.__name}.txt'
#
#     @property
#     def posada(self):
#         with open(self.__posada_file, 'r') as f:
#             all_lines = f.readlines()
#         if all_lines:
#             return all_lines[-1]
#
#     @posada.setter
#     def posada(self, value):
#         if type(value) is str:
#             with open(self.__posada_file, 'a') as f:
#                 f.write(value+'\n')
#
#     @classmethod
#     def get_ppl(cls):
#         print('Test classmethod', cls)
#
#     @staticmethod
#     def validate_age(value, min_value=0):
#         if type(value) is int:
#             if min_value < value < People.MAX_PEOPLE_AGE
#                 return True
#             return False
#
#
#
# masha =  People('Masha', 25)
# People.get_ppl()



# print(masha.age)
# masha.age = 26
# masha.office = '123 Wall Str.'
#
# dasha  = People('Dasha', 35)
# print(masha.age)
# masha.age = '2000'
# print(masha.posada) = 'Judge'




# class Human:
#     mail_pref = ''
#
#     def __init__(self, email):
#         if self.__class__.is_valid_email(email):
#             self.email = email
#         else:
#             self.email = 'No Mail.'
#
#
#     @classmethod
#     def is_valid_email(cls, email: str) -> bool:
#         return email.startswith(cls.mail_pref)
#
#     def _privet(self):
#         print('Hi from Human')

class Farmer:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animals.append(animal)

    def display_usability(self):
        for animal in self.__animals:
            print(animal.usability)

    def sell_animal(self, animal, buyer):
        if animal in self.__animals:
            self.__animals.pop(self.__animals.index(animal))
            animal.owner = buyer



class Animal:
    def __init__(self, price: int, owner: Farmer):
        self.price = price
        self.owner = owner

    @property
    def usability(self):
        return f'Can be sold for ${self.price}.'

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        if isinstance(new_owner, Farmer):
            self.__owner = new_owner
            new_owner.add_animal(self)
        else:
            print('Wrong Owner')


class Chicken(Animal):
    def usability(self):
        return f'{super().usability()} and gives some eggs.'

class Cow(Animal):
    pass
#
# class User(Human):
#     mail_pref = 'user_'
#
#
# class Admin(Human):
#     mail_pref = 'admin_'
#
#     def privet2(self):
#         return self._privet

# if __name__ == '__main__':
    # oleg = User('user_ol@gmail.com')
    # print(oleg.email)
    # oleg2 = Admin('admin_ad@gmail.com')
    # print(oleg2.email)
    # # oleg.__privet()
    # oleg2.privet2()
maks = Farmer()
koko = Chicken(9, maks)
print(koko.owner)
print(koko.usability)