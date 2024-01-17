import turtle
# it declares  specific locations
turtle.setup(300, 300)
turtle.penup()
turtle.hideturtle()
turtle.goto(-120, 120)
turtle.write("top left")
turtle.goto(70, -120)
turtle.write("bottom right")
# filling shapes
turtle.hideturtle()
turtle.fillcolor('blue')
turtle.begin_fill()
# draws a circle
turtle.circle(100)
turtle.end_fill()
# turtle .done  make screen not to cross
turtle.done()
