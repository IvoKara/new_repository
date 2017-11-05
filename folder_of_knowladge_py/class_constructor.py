class Animal:
    def __init__(self,name,color):
        self.color=color
        self.name=name

class Cat(Animal):
    def purr(self):
        print("{} says prrr..".format(self.name))

class Dog(Animal):
    legs = 4
    def bark(self):
        print("{}: WOOF!".format(self.name))

Rex = Dog("Rex","black")
print("{} is {} and has {} legs".format(Rex.name, Rex.color,Rex.legs))
Rex.bark()

Maya = Cat("Maya","orange")
print("{} is {}".format(Maya.name, Maya.color))
Maya.purr()

rabbit = Animal("John","grey")
print(rabbit.name)
#rabbit.purr()
