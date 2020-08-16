'''Task 1
Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
and make their own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’,
while Cat’s can be to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
and performs talk method on input parameter.'''

class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError('Must be used by a subclass only!')

class Dog(Animal):
    def talk(self):
        print('Woof woof!')

class Cat(Animal):
    def talk(self):
        print('Meow!')


spike = Dog('Spike')
spike.talk()

marques = Cat('Marques')
marques.talk()


def voice(animal):
    animal.talk()

voice(spike)

animals = [Dog('Jojo'), Cat('Gas'), Cat('Horus'), Dog('C.J.')]
for animal in  animals:
    animal.talk()