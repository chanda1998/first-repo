from turtle import *

ch = Pen()
ch.speed(10)
ch.color('lime')
##for  i in range(300):
##    ch.fd(i)
##    ch.rt(60)


def  star(sz):
    nsz = sz/10
    for i in range(5):
        ch.fd(sz)
        if nsz<sz:
            star(sz+20)
            nsz+=10
        ch.rt(144)
            
star(100)
