from example import circle, arc, polyline
import turtle

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, r, angle, n):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def shift(t, length):
    t.pu()
    t.fd(length)
    t.pd()

if __name__ == '__main__':
    bob = turtle.Turtle()

    shift(bob, -200)
    flower(bob, 60.0, 60.0, 7)
    shift(bob, 200)
    flower(bob, 60.0, 100.0, 8)
    shift(bob, 200)
    flower(bob, 200.0, 20.0, 20)

    # wait for the user to close the window
    turtle.mainloop()