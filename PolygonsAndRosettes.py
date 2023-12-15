import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")
sides = int(turtle.numinput("Number of sides",
                    "How many sides do you want in your spiral?"))
for m in range(5, 75):
    t.left(360/sides + 5)
    t.width(m//25+1)
    t.penup()
    t.forward(m*4)
    t.pendown()
    if (m % 2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)
turtle.done()
