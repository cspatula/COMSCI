# activitySchoolManagement.py


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


# Child class inheriting from Person
class Student(Person):
    def study(self):
        print(f"{self.name} is studying")


# Instantiate a Student object
student1 = Student("Lina", 20)

# Test inherited features and the new method
print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()} (note this age is privately accessed)")
student1.study()