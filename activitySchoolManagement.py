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


class Principal(Person):
    def manage_school(self):
        print(f"{self.name} is managing the school")

    def role(self):
        print(f"{self.name} is the principal")


class GuidanceCounselor(Person):
    def assist_students(self):
        print(f"{self.name} is assisting students")

    def role(self):
        print(f"{self.name} is a guidance counselor")


# Create and test a GuidanceCounselor object
counselor = GuidanceCounselor("Sara", 35)

print(f"Name: {counselor.name}")
print(f"Age: {counselor.get_age()}")
counselor.assist_students()
counselor.role()