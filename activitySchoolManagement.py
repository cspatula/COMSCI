from abc import ABC, abstractmethod


# 1. Abstraction & 2. Encapsulation
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Encapsulated (private) attribute

    def get_age(self):
        return self.__age

    @abstractmethod
    def role(self):  # Abstract interface
        pass


# 3. Inheritance & 4. Polymorphism
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


# Create objects and store them in a single list
people = [
    Student("Lina", 20),
    Teacher("Mona", 30),
    Principal("Mr. X", 55)
]

# Demonstrate polymorphism: one interface (role()), multiple behaviors
for person in people:
    print(f"Name: {person.name} | Age: {person.get_age()}")
    person.role()
    print("-" * 30)