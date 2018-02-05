import turtle
abscissa = turtle.Turtle()
abscissa.speed(100)
ordinata = turtle.Turtle()
ordinata.speed(100)
graphic = turtle.Turtle()
graphic.color("blue")
graphic.shape("blank")

print("f(x) = ax + b")
print("Напишете 'Yes' ако желаете x^2, 'No' ако не желаете")
while True:
    c = input()
    if c == "Yes" or c == "No":
        break
a = int(input("a: "))
b = int(input("b: "))
def funk(x):
    if c == "Yes":
        y = a*x*x + b
    else:
        y = a*x + b
    return y
print("\n 1 = 20px")

def printGraph(funk, x1, x2, y1, y2):
    if x1 <= 0 and y1 <= 0:
        pass
    elif x1 <= 0 and y1 > 0:
        y1 = -y1
    elif x1 > 0 and y1 <= 0:
        x1 = -x1
    else:
        x1 = -x1
        y1 = -y1

    if x1 != 0:
        n = x1
    else:
        n = x2
    abscissa.goto(x1*20,0)
    ordinata.goto(0,y1*20)
    i1 = abs(x1)+x2
    for _ in range(int(i1)):
        abscissa.left(90)
        abscissa.forward(2)
        abscissa.back(4)
        abscissa.forward(2)
        abscissa.right(90)
        abscissa.forward(20)
    i2 = abs(y1)+y2
    ordinata.left(90)
    for _ in range(int(i2)):
        ordinata.left(90)
        ordinata.forward(2)
        ordinata.back(4)
        ordinata.forward(2)
        ordinata.right(90)
        ordinata.forward(20)

    if funk(x1) < y1 or funk(x1) > y2:
        while True:
            x1 = x1 + 1
            if funk(x1) <= y1 or abs(funk(x1)) <= y2:
                break
    graphic.up()
    for _ in range(int(i1)+int(i2)):
        if (x1 > x2 or funk(x1) > y2)\
        or (funk(x1) < y1 or x1 > abs(n)):
            break
        graphic.goto(x1*20,funk(x1)*20)
        graphic.down()
        x1 = x1 +1

        
x1 = int(input("Начало на абсциса: "))
x2 = abs(int(input("Край на абсциса: ")))
y1 = int(input("Начало на ордината: "))
y2 = abs(int(input("край на ордината: ")))

printGraph(funk,x1,x2,y1,y2)

    
    
