import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def koch(t, length):
    angle = 60
    if length < 10:
        t.fd(length)
        return
    koch(t, length/3)
    t.lt(angle)
    koch(t, length/3)
    t.rt(angle*2)
    koch(t, length/3)
    t.lt(angle)
    koch(t, length/3)

def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        t.rt(120)

if __name__ == '__main__':
    bob = turtle.Turtle()

    bob.pu()
    bob.goto(-150, 90)
    bob.pd()
    snowflake(bob, 300)

    # wait for the user to close the window
    turtle.mainloop()