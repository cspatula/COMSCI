# activitySchoolManagement.py


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Fixed: Added double underscore to make it private

    def get_age(self):
        return self.__age
    
# Instantiate the object person1
person1 = Person("Lina", 20)

# Display its information using person1 (lowercase 'p')
print(f"Name: {person1.name}")
print(f"Age: {person1.get_age()} (note this age is privately accessed)")

# Reflection: Why is it better to access __age through get_age()?
# Using get_age() protects the private data from accidental direct changes 
# and gives us control over how the value is accessed.