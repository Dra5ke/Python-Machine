import turtle
import math

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length =    circumference / n
    polygon(t, n, length)


def centerTurtle(t, length):
    t.pu()
    t.lt(180)
    t.fd(length)
    t.lt(90) 
    t.fd(length)
    t.lt(90)
    t.pd()

bob = turtle.Turtle()
circle(bob, 20)
turtle.mainloop()