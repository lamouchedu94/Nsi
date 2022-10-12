import turtle
turtle.tracer(0, 0) 
turtle.penup()
turtle.goto([-200, 200])
turtle.pendown()
#turtle.done()
 
turtle.penup() 
def carre3(n):
    turtle.speed(0)
    if n <= 1 :
        for i in range(4):
            turtle.forward(n)
            turtle.right(90)
    else : 
        carre3(n/3)
        turtle.forward(n/3)
        carre3(n/3)
        turtle.forward(n/3)
        carre3(n/3)
        turtle.forward(n/3)
        turtle.left(180)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n/3)
        turtle.left(90)
        carre3(n/3)
        turtle.forward(n/3)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(n/3)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(n/3)
        carre3(n/3)
        turtle.forward(n/3)
        turtle.left(180)
        turtle.forward(n)
        turtle.left(90)
        turtle.forward(n/3)
        turtle.left(90)
        carre3(n/3)
        turtle.forward(n/3)
        carre3(n/3)
        turtle.forward(n/3)
        carre3(n/3)
        turtle.forward(n/3)
        turtle.left(180)
        turtle.forward(n)
        turtle.right(90)
        turtle.forward(2*n/3)
        turtle.right(90)
 
 
carre3(300)
#base(300)
 
 
 
turtle.update()	
 
turtle.done()