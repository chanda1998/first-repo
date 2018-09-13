from turtle import *

a = Pen()
b = Pen()
c = Pen()
d = Pen()
a.speed('fastest')
c.speed('fastest')
b.speed('fastest')
d.speed('fastest')
b.rt(90)
c.rt(45)
d.rt(135)
i=0
colors = ['pink', 'yellow', 'skyblue', 'lightgreen']
while True:
    for color in colors:
        a.pencolor(color)
        b.pencolor(color)
        c.pencolor(color)
        d.pencolor(color)
        if i%2 == 0:
            a.circle(10+i)
            b.circle(10+i)
            c.circle(10+i)
            d.circle(10+i)
        else:
            a.circle(-10-i)
            b.circle(-10-i)
            c.circle(-10-i)
            d.circle(-10-i)
    
        i+=1

