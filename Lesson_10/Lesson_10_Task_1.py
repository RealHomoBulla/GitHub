'''
Task 1
A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters
and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing,
for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.'''

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")


cj = Person('Carl', 'Johnson', 26)
# If we do not create method __repr__, printing our Class instance will give only Python-look object info.
print(cj)

# To call it in required way we have to call it like this, or create __repr__ method.
cj.talk()