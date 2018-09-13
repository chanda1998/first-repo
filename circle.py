from turtle import *




# a flower of circle
ch = Pen()
ch.speed('fastest')
ch.color('red')
i = 0
while True:
    ch.circle(10+i)
    ch.rt(45)
    i+=2
    if i>400:
        break

a = 0
ch.color('green')
while True:
    ch.circle(10+a)
    ch.rt(45)
    a+=2
    if a>200:
        break

c = 0
ch.color('yellow')
while True:
    ch.circle(10+c)
    ch.rt(45)
    c+=2
    if c>100:
        break

clearscreen()

go = Pen()
go.ht()
go.pensize(10)
go.color('purple')
go.circle(100)
go.up()
go.lt(90)
go.fd(120)
go.lt(90)
go.fd(-40)
go.down()
go.circle(5)
go.up()

go.backward(-80)
go.down()
go.circle(5)
go.up()
go.lt(90)
go.fd(60)
go.lt(90)
go.fd(10)
go.rt(90)
go.down()
go.circle(30, 180)









write('thank you', font=('', 16))







