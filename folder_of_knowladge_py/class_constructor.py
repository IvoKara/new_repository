class Animal:
    def __init__(self,name,color): #self is the instance that is called auto
        self.color=color
        self.name=name
    def __name__(self):
        return "Animal"
class Cat(Animal):
    def purr(self):
        print("{} says prrr..".format(self.name))

class Dog(Animal):
    legs = 4
    def bark(self):
        print("{}: WOOF!".format(self.name))
    def __str__(self):
        return "The dog called {} has {} fur".format(self.name,self.color)

Rex = Dog("Rex","black")
print("{} is {} and has {} legs".format(Rex.name, Rex.color,Rex.legs))
print(Dog.bark(Rex) == Rex.bark())
print(Rex)

Maya = Cat("Maya","orange")
print("{} is {}".format(Maya.name, Maya.color))
Maya.purr()
print(Maya)

rabbit = Animal("John","grey")
print(rabbit.name)
#rabbit.purr()
print(rabbit.__dict__)
print(rabbit.__module__)
print(rabbit.__name__())

print(Animal(Maya))