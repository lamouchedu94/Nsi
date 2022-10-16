import turtle
turtle.tracer(0)
def triangle(l, lmin) :
    if l < lmin :
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(l)
            turtle.left(120)
        turtle.end_fill()
    else :
        #
        triangle(l/2, lmin)
        turtle.forward(l/2)
        triangle(l/2, lmin)
        turtle.backward(l/2)
        turtle.left(60)
        turtle.forward(l/2)
        turtle.right(60)
        triangle(l/2, lmin)
        turtle.left(60)
        turtle.backward(l/2)
        turtle.right(60)
turtle.begin_fill()
for i in range(3) :
    turtle.forward(500)
    turtle.left(120)
turtle.end_fill()
turtle.fillcolor("white")
triangle(500, 3)

turtle.update()
turtle.done()

