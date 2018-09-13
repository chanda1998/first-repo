from turtle import *
t = Pen()
bgcolor('black')
w=Screen()

t.speed('fastest')
col = ['orange', 'white', 'green']
for co in col:
    t.pencolor(co)
    for i in range(4):
        t.lt(30)
        while True:
            t.fd(200)
            t.lt(170)
            if abs(t.pos()) < 1:
                break

t.reset()

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
colors = ['red', 'yellow', 'skyblue', 'blue']
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
