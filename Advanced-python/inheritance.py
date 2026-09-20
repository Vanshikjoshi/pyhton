# inheritance:parent-child relation
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
