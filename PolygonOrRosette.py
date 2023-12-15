import turtle
t = turtle.Pen()
t.speed(0)
t.color("white")
turtle.bgcolor("black")
number = int(turtle.numinput("Number of sides or circles",
                        "How many sides or circles do you want in your shape?"))
shape = turtle.textinput("Which shape do you want?",
                         "Enter 'p' for polygon or 'r' for rosette")
for x in range(number):
    if shape == 'r':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)
turtle.done()
