from example import circle, arc, polyline
import turtle

def spiral(t, length, n, a, b):
    theta = 0.0
    for i in range(n):
        t.fd(length)
        step_turn = 1 / (a + b*theta)
        t.lt(step_turn)
        theta += step_turn

if __name__ == '__main__':
    bob = turtle.Turtle()

    spiral(bob, 3.5, 200, 0.01, 0.0002)

    # wait for the user to close the window
    turtle.mainloop()