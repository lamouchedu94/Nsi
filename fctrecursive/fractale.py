import turtle


#taille 100
turtle.tracer(0, 0) 
def fractale(n = 600):
#    turtle.speed(0)
    if n <= 1 :
        turtle.forward(n)
    else :
        fractale(n/3)
        turtle.left(60)
        fractale(n/3)
        turtle.right(120)
        fractale(n/3)
        turtle.left(60)
        fractale(n/3)
turtle.penup()
turtle.goto([-300,300])
turtle.pendown()
for i in range(3):
    fractale()
    turtle.right(120)


"""
turtle.forward(600)
turtle.right(120)
turtle.forward(600)
turtle.right(120)
turtle.forward(600)
turtle.right(120)
"""
turtle.hideturtle()
turtle.update()	
turtle.done()