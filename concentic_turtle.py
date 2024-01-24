import  turtle
num=20
startRadius=20
offset=10
AnimalSpeed=0
turtle.speed(AnimalSpeed)
turtle.hideturtle()
radius=startRadius
for count in range(num):
    turtle.circle(radius)
    x=turtle.xcor()
    y=turtle.ycor() -offset
    radius=radius + offset
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    