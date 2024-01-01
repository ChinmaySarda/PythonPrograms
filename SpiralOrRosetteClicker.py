import turtle
import random
t = turtle.Pen()
t.hideturtle()
t.speed(0)
t.pencolor("white")
turtle.bgcolor("black")
shape = turtle.textinput("Do you want a clicky spiralor a rosette?",
                         "Type [s] for a spiral or [r] for a rosette.").lower()
if shape == "s":
    sides = turtle.numinput("Sides", "How many sides do you want in your spiral?")
    def spiral(x,y):
        t.penup()
        t.setpos(x,y)
        t.pendown()
        for x in range(random.randint(10, 30)):
            t.forward(x*2)
            t.left(360/sides)
    turtle.onscreenclick(spiral)
elif shape == "r":
    circles = turtle.numinput("circles", "How many circles do you want in your rosette?")
    def circle(x,y):
        t.penup()
        t.setpos(x,y)
        t.pendown()
        for x in range(random.randint(10, 30)):
            t.circle(x)
            t.left(360/circles)
    turtle.onscreenclick(circle)
else:
    t.write("There was an error, try again.")
turtle.done()
