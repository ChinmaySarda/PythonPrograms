import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
noc = int(turtle.numinput("Number of circles",
                                "How many circles do you want in your rosette?"))
for x in range(noc):
    t.pencolor("red")
    t.circle(100)
    t.pencolor("yellow")
    t.circle(50)
    t.left(360/noc)
t.hideturtle()
turtle.done()
