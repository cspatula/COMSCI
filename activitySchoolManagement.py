# activitySchoolManagement.py
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    @abstractmethod
    def role(self):
        pass


class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

    def role(self):
        print(f"{self.name} is a student")


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

    def role(self):
        print(f"{self.name} is a teacher")


# Test concrete subclasses
student = Student("Lina", 20)
teacher = Teacher("Mona", 30)

student.role()
teacher.role()

# Attempting to instantiate Person directly raises a TypeError:
# p = Person("Ali", 25)  # TypeError: Can't instantiate abstract class Person without an implementation for abstract method 'role'