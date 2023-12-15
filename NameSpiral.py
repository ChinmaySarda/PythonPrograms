import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
yourname = turtle.textinput("Enter your name.", "What is your name?")
for x in range(100):
    t.pencolor( colors[ x % 4] )
    t.penup()
    t.forward( x * 4 )
    t.pendown()
    t.write(yourname, font = ("Arial", int((x + 4) / 4), "bold"))
    t.left(92)
turtle.done()
