import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = int(turtle.numinput("number of sides",
                            "How many sides do you want (1-10)?", 4, 1, 10)) 
colors = ["red", "yellow", "blue", "orange", "green", "purple",
          "gray", "light blue", "pink", "white"]
for x in range(360):
    t.pencolor( colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
turtle.done()
