import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "orange", "green",
          "purple", "gray", "light blue", "pink", "light green"]
yourname = turtle.textinput("Enter your name.", "What is your name?")
sides = int(turtle.numinput("number of sides",
                             "How many sides do you want (1-10)?", 5, 1, 10)) 
for x in range(100):
    t.pencolor(colors[x%sides%10])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(yourname, font=("Arial", int((x*2 + 4) / 4), "bold"))
    t.left(360/sides+2)
turtle.done()
