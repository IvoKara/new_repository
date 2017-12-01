class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def __init__(self, name, color, color_eyes):
        super().__init__(name,color)
        #self.typ = typ
    def bark(self):
        print("Woof")
        super().bark()
class Husky(Dog):
    def Name(self):
        print("Go there ", self.name)

class Lion:
    pass

class Console:
    def WriteLine(word):
        print(word)

##Skala = Wolf("Skala", "white")
##print(Skala.bark())
##print(Skala)

Ivo = Dog("Ivo", "Blue", "Blue")
print(Ivo.bark())

Mark = Husky("Mark","blue","Husky")
Mark.Name()
Mark.bark()
print(Mark.name)


Dogo = Husky("Dogo", "black", "blue")
print(Dogo.Name)

Console.WriteLine("Hello SoftUni!")
