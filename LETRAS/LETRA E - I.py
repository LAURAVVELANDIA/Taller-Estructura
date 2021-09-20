import turtle 


tortuga=turtle.Turtle()
tortuga.pensize(15)
tortuga.color("blue")
tortuga.shape('turtle')
tortuga.left(180)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(80)
tortuga.left(180)
tortuga.forward(80)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(100)



tortuga=turtle.Turtle()
tortuga.shape('turtle')
tortuga.pensize(15)
tortuga.color("blue")
tortuga.penup()
tortuga.goto((105, 0))
tortuga.pendown()
tortuga.forward(120)
tortuga.right(180)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(120)
tortuga.right(90)
tortuga.forward(60)
tortuga.left(180)
tortuga.forward(120)




    


t=turtle.Turtle()
t.speed(0)
t.penup()
t.goto((335, -120))
t.pendown()
t.pencolor("pink")
t.pensize(5)



for x in range (6):
    t.rt(60)
    for y in range (9):
        t.fd(10)
        t.rt(10)
    t.rt(90)
    for z in range (9):
        t.fd(10)
        t.rt(10)
    t.rt(90)