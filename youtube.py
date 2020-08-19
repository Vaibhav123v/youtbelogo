import turtle
t = turtle.Turtle()
t.up()
t.goto(-60,40)
t.down()
t.fillcolor("red")
t.begin_fill()
t.forward(250)
t.setheading(270)
s = 360
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

    
t.forward(100)
s = 270
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(250)
s = 180
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)

t.forward(100)
s = 90
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.end_fill()
t.up()
t.forward(70)
t.setheading(270)
t.forward(40)
t.down()
t.fillcolor("white")
t.begin_fill()
t.forward(130)
t.setheading(0)
t.setheading(30)
t.forward(130)
t.setheading(150)
t.forward(130)
t.end_fill()
t.hideturtle()

