import turtle
t = turtle.Turtle()
t.color("blue")
t.fillcolor("pink")
t.begin_fill()
for i in range(1, 5, 1):
    t.forward(100)
    t.left(90)
t.end_fill()
t.penup()
t.goto(120,120)
t.pendown()
t.circle(80)
# t.right(50)
# t.left(150)
t.backward(100)#shortform bk
# t.forward(90)#shortform fd
turtle.mainloop()