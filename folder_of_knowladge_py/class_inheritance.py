class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")
        super().bark()
class Husky(Dog):
    def Name(self):
        print("Go there ", self.name)

Mark = Husky("Mark","blue")
Mark.Name()
Mark.bark()
