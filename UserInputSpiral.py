import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = turtle.textinput("Number of sides",
                        "Enter a number of sides between 2 and 10: ")
colors = ["red", "yellow", "blue", "orange", "green", "purple", "gray", "light blue", "pink", "light green"]
for x in range(360):
    t.pencolor(colors[x%int(sides)])
    t.forward(x * 3 / int(sides) + x)
    t.left(360/int(sides) + 1)
    t.width(x*int(sides)/100)
turtle.done()
