class Semeistvo():
    pass
class roditeli(Semeistvo):
    def eat(self):
        print("eat food")
    def wlak(self):
        print("walk")
    def sleep(self):
        print("sleep")
class deca(roditeli):
    pass

class Animals():
    def breathe(self):
        print("breathing")
    def move(self):
        print("moving")
    def eat_food(self):
        print("eating")
class Mammals(Animals):
    def feed_young_with_milk(self):
        slef.eat_food()
        print("feed Younf with milk")
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        self.move()
        self.eat_food()
        print("eat leaves from trees")
    def __init__(self, dots):
        self.madafaka=dots
        
reginald = Giraffes(90)

reginald.move()
reginald.eat_leaves_from_trees()
print(reginald.madafaka)

