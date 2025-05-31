#Super 

class Parent:
    def __init__(self):
        self.__private_var = "I'm private"
        self.public_var = "I'm public"

    def show(self):
        return self.__private_var

class Child(Parent):
    def __init__(self):
        super().__init__()
        # Trying to access __private_var directly
        try:
            print(self.__private_var)
        except AttributeError:
            print("❌ Can't access private variable directly in subclass")

        # But we can access public_var
        print("✅ Public var from parent:", self.public_var)

        # We can access private variable using name mangling
        print("🔓 Access using mangled name:", self._Parent__private_var)

child = Child()

#Example 2:

class Animal:
    def __init__(self):
        print("Animal is alive")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog is born")

d = Dog()


#Example:
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

s = Student("Aniruddhan", 1682)
print(s.name, s.roll_no)
