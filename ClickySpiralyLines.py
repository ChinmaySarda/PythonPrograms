import random
import turtle
t = turtle.Pen()
t.hideturtle()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange",
          "purple", "white", "gray", "pink", "brown"]
def spiral(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    t.setpos(x,y)
    for m in range(size):
        t.forward(m*2)
        t.left(91)
turtle.onscreenclick(spiral)
turtle.done()
