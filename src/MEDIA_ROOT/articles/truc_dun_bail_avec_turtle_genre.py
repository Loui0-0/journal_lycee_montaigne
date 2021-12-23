import turtle as t
from math import *
t.hideturtle()
y = 0
x = 0
t.setworldcoordinates(0,-500,1000,500)
t.delay(0)
t.speed(0)
while 1:
    x += 0.0001
    y += 0.001
    xx = x*10000
    yy = sin(tan(x))*20    
    t.goto(xx - 15000,yy)
