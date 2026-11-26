# activitySchoolManagement.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")


# Test the Teacher class
teacher = Teacher("Mona", 30)

print(f"Name: {teacher.name}")
print(f"Age: {teacher.get_age()}")
teacher.teach()