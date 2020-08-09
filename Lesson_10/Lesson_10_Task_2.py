'''Task 2
Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.'''

class Dog:
  age_factor = 7
  
  def __init__(self, age):
    self.age = age

  def human_age(self):
    self.equivalent_age = self.age * self.age_factor
    return f'{self.age} years dog age is equivalent to {self.equivalent_age} years of human age.'

snoop_dog = Dog(14)
print(snoop_dog.human_age())