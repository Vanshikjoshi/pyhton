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
