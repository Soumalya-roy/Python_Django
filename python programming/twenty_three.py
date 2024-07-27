class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Derived class must implement this function")
class Cat(Animal):
    def talk(self):
        return "Meow"
class Dog(Animal):
    def talk(self):
        return "Bhow-Bhou"
animals = [Cat("Kit"),Cat("bilota"),Dog("Ruff"),Cat("Eve"),Dog("Grom")]
for animal in animals:
    print(animal.name,"-",animal.talk())