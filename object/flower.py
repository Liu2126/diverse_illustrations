import turtle as t
t.speed(0)
t.penup()
t.goto(-50, 0)
t.pendown()
t.pencolor("black")
t.setheading(90)
t.pensize(5)
t.circle(-50,360)

t.pencolor("red")
t.setheading(180)
t.circle(-50,270)

t.pencolor("green")
t.setheading(90)
t.circle(-50,270)

t.pencolor("yellow")
t.setheading(0)
t.circle(-50,270)

t.pencolor("blue")
t.setheading(270)
t.circle(-50,270)

t.penup()
t.goto(0,-50)
t.pendown()
t.pencolor("pink")
t.setheading(270)
t.circle(1000,30)
t.done()