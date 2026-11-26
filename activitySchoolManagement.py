# activitySchoolManagement.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age


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


# Create objects for both classes
student = Student("Lina", 20)
teacher = Teacher("Mona", 30)

# Test Student
print(f"Name: {student.name}")
print(f"Age: {student.get_age()}")
student.study()
student.role()

print("-" * 20)

# Test Teacher
print(f"Name: {teacher.name}")
print(f"Age: {teacher.get_age()}")
teacher.teach()
teacher.role()