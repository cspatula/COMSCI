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


# Create objects for all classes
student = Student("Lina", 20)
teacher = Teacher("Mona", 30)
principal = Principal("Mr. X", 55)

# Test Student
print(f"Name: {student.name}")
print(f"Age: {student.get_age()}")
student.study()
student.role()

print("-" * 25)

# Test Teacher
print(f"Name: {teacher.name}")
print(f"Age: {teacher.get_age()}")
teacher.teach()
teacher.role()

print("-" * 25)

# Test Principal
print(f"Name: {principal.name}")
print(f"Age: {principal.get_age()}")
principal.manage_school()
principal.role()