class Animal:
    def makeSound(self):
        print("Sound of Animals")

class Dog(Animal):
    def makeSound(self):
        super().makeSound()
        print("Sound of Dog is bark")
class Cat(Animal):
    def makeSound(self):
        super().makeSound()
        print("Sound of Cat is meuw")
class Tiger(Animal):
    def makeSound(self):
        super().makeSound()
        print("Sound of Tiger is Roar")
d = Dog()
d.makeSound()

c = Cat()
c.makeSound()

t = Tiger()
t.makeSound()
