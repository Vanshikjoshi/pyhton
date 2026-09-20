# inheritance:parent-child relation
"""
class Animal:
    def eat(self):
        print("Eating")


# class Child_class_name(parent_class_name)
class Dog(Animal):
    def bark(self):
        self.eat()
        print("Woof!")


d = Dog()
d.bark()
"""

# method overriding
"""
----------------------------------------
class Animal:
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    def speak(self):
        print("Dog is barking")


class Cat(Animal):
    def speak(self):
        print("Cat is meowing")


d = Dog()
c = Cat()
d.speak()  # dog speak method override the animal speak method
-------------------------------------------
"""
# super function
"""
------------------------------
class Animal:
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog is barking")


d = Dog()
d.speak()
----------------------------------------
"""


# types of inheritance
"""
----------------------------
# 1-single inheritance
class Parent:
    def speak(self):
        print("Hello from parent")


class Child(Parent):
    def speak(self):
        super().speak()
        print("Hello from child")
c = Child()
c.speak()
---------------------------------
"""

"""
---------------------------------
# 2-multilevel inheritance
class Grandparent:
    def speak(self):
        print("Hello from grandparent")


class Parent(Grandparent):
    def greet(self):
        print("Hello from parent.")


class Child(Parent):
    def show(self):
        super().greet()
        print("Hello from child!")


c = Child()
c.show()
c.speak()
-----------------------------------------
"""


# 3-hiearchical inheritance
"""
--------------------------------
class Animal:
    def speak(self):
        print("Animal is speaking")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal):
    def meow(self):
        print("Cat is meowing")
d = Dog()
d.speak()
d.bark()
c = Cat()
c.speak()
c.meow()
------------------------------------
"""


# 4-Multiple inheritance:one-child multiple parent
class P1:
    def show(self):
        print("Hello from parent1")


class P2:
    def greet(self):
        print("Hello from parent2")


class Child(P1, P2):
    def speak(self):
        print("Hello from child")


c = Child()
c.speak()
c.greet()
c.show()
