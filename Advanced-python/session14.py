# oops concept
class Student:
    pass


# pass means empty body
stdude1 = Student()
print(stdude1)


class Std:
    """
    roll = 0
    name = ""
    gender = ""
    age = 0
    """

    # methods
    """
    def set(self):
        self.roll = int(input("Enter roll no.: "))
        self.name = input("Enter name: ")
        self.gender = input("Enter gender: ")
        self.age = int(input("Enter age: "))
    """

    # methods using parameters
    """
    def set(self, r: int, n: str, g: str, a: int) -> None:
        self.roll = r
        self.name = n
        self.gender = g
        self.age = a
    """

    # initialisaing using constructor
    def __init__(self, r: int, n: str, g: str, a: int) -> None:
        self.roll = r
        self.name = n
        self.gender = g
        self.age = a

    # Methods
    def display(self):
        print("The details are: ")
        print(f"Roll no: {self.roll}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")


"""
std1 = Std()
std1.roll = 89
std2 = Std()
std1.name = "Vanshika"
std1.gender = "Female"
std1.age = 45
std1.display()
std2.display()
"""
# after using set method
"""
std1 = Std()
std2 = Std()
std1.set(23, "Abc", "Male", 34)
std2.set(678, "xyz", "female", 23)
std1.display()
std2.display()
"""
# after using constructor
std1 = Std(1, "Abc", "Female", 23)
std1.display()
