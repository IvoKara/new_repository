import turtle
graph = turtle.Turtle()
graph.color("blue")
graph.shape("blank")
def max_height():
    return 300
def max_width():
    return 350
#def draw_lines(kind,lenght,scale,nums=False)
def draw_abs(lenght, scale,nums=False):
    lenght=scale*lenght
    abscissa = turtle.Turtle()
    abscissa.up()
    for i in range(-lenght,lenght+1,scale):
        abscissa.goto(i,2)
        abscissa.down()
        if nums:
            font=("Airal",6,"normal")
            if i!=0:
                if scale<=10 and i%5!=0:# scalex
                    font=("Arial",5,"normal")
                    abscissa.shapesize(0.5,0.5,0)
                else:
                    abscissa.write(int(i/scale),align="center",font=font)
        abscissa.goto(i,-2)
        abscissa.goto(i,0)
        abscissa.forward(scale)

def draw_ord(lenght, scale,nums=False):
    lenght=scale*lenght
    ordinata = turtle.Turtle()
    ordinata.up()
    ordinata.left(90)
    for i in range(-lenght,lenght+1,scale):
        ordinata.goto(-2,i)
        ordinata.down()
        if nums:
            font=("Airal",6,"normal")
            if scale<=10 and i%5!=0:# scaley 
                font=("Arial",5,"normal")
                ordinata.shapesize(0.5,0.5,0)
            else:
                ordinata.write(int(i/scale),align="right",font=font)
        ordinata.goto(2,i)
        ordinata.goto(0,i)
        ordinata.forward(scale)

if __name__=="__main__":     
    print("f(x) = ax + b")
    a = int(input("a: "))
    b = int(input("b: "))
    print("f(x) = {}x + {}".format(a,b))
    scl=30
    def funk(x):
        return a*x+b
    
    def zero_cor(scale):
        global max_x,max_y
        y0=funk(0)
        x0=y0
        if a!=0:
            x0=-b/a
        max_x=abs(x0)+2
        max_y=abs(y0)+2
        while max_y*scale>=max_height() or max_x*scale>=max_width():
            scale-=1
        if x0<0:
            max_x*=-1
        if y0<0:
            max_y*=-1
        return scale
    
    scl=zero_cor(scl)

    def draw_graph(scale):
        draw_abs(round(abs(max_x)),scale,True) #scalex   
        draw_ord(round(abs(max_y)),scale,True) #scaley
        graph.up()
        for x in max_x,-max_x:
            y=funk(x)
            while abs(y)>abs(max_y):
                if x>0:     
                    x=round(x-0.01,2)
                else:
                    x=round(x+0.01,2)
                y=funk(x)
            graph.goto(x*scale,y*scale)
            graph.down()
            
        
        '''
        graph.goto(x0*scale,0)
        graph.write(x0,align="right",font=("Arial",5,"normal"))     #format it
        graph.down()
        graph.goto(0,y0*scale)
        graph.write(y0,align="right",font=("Arial",5,"normal"))     #format it
'''
    draw_graph(scl)
#turtle.done()
