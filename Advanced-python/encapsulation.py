# encapsulation - hiding data
"""
class Bank:
    def __init__(self, name: str, balance: int, bank_name: str) -> None:
        self.name = name  # public
        self._bank_name = bank_name  # protected
        self.__balance = balance  # private

    def deposit(self, amount: int):
        if amount < 0:
            print("Invalid amount")
        else:
            self.__balance += amount
            print(f"Balance is: {self.__balance}")


c1 = Bank("anirudh", 1000, "abc bank")
c1.deposit(200)
# c1.balance = 200 // not possible
c1.deposit(-2)
# in python it is not real security because we can still access the private members like-
print(c1._Bank__balance)
# even we have made the balance private but still we can access this ;
------------------------------------------------
"""

"""
# getter and Setter
class Student:
    def __inti__(self, name) -> None:
        self._name = name

    # getter
    def get_name(self):
        return self._name

    # setter
    def set_name(self, new_name: str):
        self._name = new_name

s1 = Student("Vanshika")
print(s1.get_name())
(s1.set_name("Radhika"))
print(s1.get_name())
"""


# @property decorator-getter & setter new way
class Person:
    def __init__(self, age: int):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age can't be negative")
        self._age = value


p = Person(22)
print(p.age)
p.age = 25
print(p.age)
p.age = -5
