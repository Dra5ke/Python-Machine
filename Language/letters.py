import turtle
import math

def draw_a(t, size):
    angle = 72
    h = size * math.sin(angle) 
    t.lt(angle)
    t.fd(size)
    t.rt(36)
    t.fd(2)
    t.lt(72)
    t.fd( math.sqrt( 4 * ( 4 - h/4 )) )
    t.rt(72)
    t.fd(2)
    t.rt(36)
    t.fd(size)
