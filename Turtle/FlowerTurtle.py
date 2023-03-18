import turtle
t = turtle.Turtle()
t.color("cyan","yellow")
turtle.bgcolor("black")
t.speed(0)
n=0
t.begin_fill()
while n<10:
    for i in range(40):
        t.fd(100)
        t.left(175)
    t.circle(100)
    for i in range(40):
        t.fd(200)
        t.left(175)
    n+=1
t.end_fill()

turtle.done()