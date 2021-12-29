import turtle

a = 0
b = 0
c= 0
turtle.bgcolor('black')
turtle.speed(0)
turtle.pencolor('green')
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()



while True:
    turtle.forward(a)
    turtle.right(b)
    turtle.left(c)
    
    a+=1.5
    b+=1
    c+=0.1