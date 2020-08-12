'''Task 1
School
Make a class structure in python representing people at school. Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher. '''

class Person:
    def __init__(self, name, gender, age, hair_color, height):
        self.name = name
        self.gender = gender
        self.age = age
        self.hair_color = hair_color
        self.height = height


class Student(Person):
    def __init__(self, name, gender, age, hair_color, height, grades_list, attendance_percentage, patron):
        super().__init__(name, gender, age, hair_color, height)
        self.grades_list = grades_list
        self.attendance_percentage = f"{attendance_percentage} %"
        self.patron = patron.name

    def bullying(self, other_student):
        return f"I'll kill you, {other_student}!"


class Teacher(Person):
    def __init__(self, name, gender, age, hair_color, height, rank):
        super().__init__(name, gender, age, hair_color, height)
        self.rank = rank

    def get_paid(self, total_working_days, basic_hourly_salary=18,  overtime_hours=10):
        self.total_working_days = total_working_days
        self.basic_hourly_salary = basic_hourly_salary
        self.overtime_hours = overtime_hours
        total_salary = self.total_working_days * (self.basic_hourly_salary * 8) + self.overtime_hours * 3
        return f"{self.name}'s salary is {total_salary}$ this month."

    def stop_bullying(self, student_name, patron_name):
        return f"Stop it now or I'm gonna call your mom {patron_name}, {student_name}!"

    def print_rank(self):
        return f"{self.name} is #{self.rank} teacher is school!"


# Creating instances
bobs_mom = Person('Ann', 'Female', 47, 'Brown', 169)
bob = Student('Bob', 'Male', 15, 'Black', 173, [3, 2, 5, 4, 5, 1, 3, 4, 4, 5], 63, bobs_mom)
mrs_anderson = Teacher('Mrs. Anderson', 'Female', 53, 'Blond', 177, 10)


print(bobs_mom.hair_color)
print(bob.name)
print(bob.attendance_percentage)
print(bob.bullying('Mike'))
print(mrs_anderson.get_paid(24, overtime_hours=15))
print(mrs_anderson.stop_bullying(bob.name, bob.patron))
print(mrs_anderson.print_rank())
print(bob.grades_list)