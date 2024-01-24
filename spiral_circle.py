import turtle
num=36
radius=100
Angle=10
Animal_speed=0
turtle.speed(Animal_speed) # set animation speed
# draw 36 circles  with the turtle tilted
# by 10 degrees after each circle  is drawn
for x in range(num):
    turtle.circle(num)
    turtle.left(Angle)