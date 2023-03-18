# blank circle in middle
import turtle

t = turtle.Turtle()
t.speed(50)

for i in range(36):
    t.circle(100)
    t.left(10)
    t.fd(10)

turtle.done()