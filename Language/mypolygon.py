import turtle
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
bob = turtle.Turtle()
print(bob)
bob.pu()
bob.lt(180)
bob.fd(50)
bob.rt(180)
bob.pd()
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()
