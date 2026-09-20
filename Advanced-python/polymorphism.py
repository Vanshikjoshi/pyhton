class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


class Cow:
    def speak(self):
        print("Moo!")


animals = [Dog(), Cat(), Cow()]
for i in animals:
    i.speak()
