
def wiatrak():
    import turtle

    t = turtle.Turtle()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)
    for i in range(6):
        t.fillcolor('red')
        t.begin_fill()
        t.forward(100)
        t.right(45)
        t.forward(25)
        t.left(135)
        t.forward(75)
        t.left(225)
        t.forward(200)
        t.left(-45)
        t.right(180)
        t.forward(83)
        t.left(90)
        t.forward(250)
        t.end_fill()
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.left(180)
        t.right(60)
        ## kolejne trojkaty
    for i in range(6):
        t.fillcolor('green')
        t.begin_fill()
        t.right(30)
        t.forward(50)
        t.right(45)
        t.forward(12)
        t.left(135)
        t.forward(37)
        t.left(225)
        t.forward(100)
        t.left(-45)
        t.right(180)
        t.forward(41)
        t.left(90)
        t.forward(125)
        t.end_fill()
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.left(180)
        t.right(30)



wiatrak()

