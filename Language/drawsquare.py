import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def centerTurtle(t, length):
    t.pu()
    t.lt(180)
    t.fd(length)
    t.lt(90) 
    t.fd(length)
    t.lt(90)
    t.pd()

bob = turtle.Turtle()
centerTurtle(bob, 200)
square(bob, 400)
turtle.mainloop()