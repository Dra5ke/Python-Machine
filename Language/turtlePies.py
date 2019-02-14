from example import polygon, polyline
from turtleFlowers import shift
import turtle
import math

def pie(t, n, r):
    angle = 360.0 / n
    for i in range(n):
        triangle(t, r, angle/2)
        t.lt(angle)

def triangle(t, r, angle):
    
    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

bob = turtle.Turtle()

shift(bob, -200)
pie(bob, 5, 100)
shift(bob, 200)
pie(bob, 6, 100)
shift(bob, 200)
pie(bob, 7, 100)

turtle.mainloop()