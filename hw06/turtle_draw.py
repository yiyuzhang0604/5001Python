import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen_size = 1500
screen.setup(screen_size, screen_size)
x1 = 0
y1 = -200
t.setpos(x1, y1)
t.color("blue", "cyan")
t.begin_fill()
t.circle(263)
t.end_fill()
t.penup()
x2 = -250
y2 = 143
t.goto(x2, y2)
t.pendown()
t.color("red", "yellow")
t.begin_fill()
length = 500
angle = 144
for i in range(5):
    t.forward(length)
    t.right(angle)

t.end_fill()
t.hideturtle()
screen.exitonclick()
