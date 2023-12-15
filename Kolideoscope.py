import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
for n in range(25):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    angle = t.heading()
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.left(91)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.left(91)
random.done()
turtle.done()
