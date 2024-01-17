import turtle
# i used to display various locations in murang'a county
turtle.setup(900, 800)
turtle.penup()
turtle.hideturtle()
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 2000
RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180
LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20
MIDDLE_BELTSTAR_X = 0
MIDDLE_BELSTAR_Y = 0
RIGHT_BELSTAR_X = 400
RIGHT_BELSTAR_Y = 20
LEFT_KNEE_X = 120
LEFT_KNEE_Y = -180
RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140
turtle.goto(LEFT_SHOULDER_X,  LEFT_SHOULDER_Y)
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELSTAR_Y)
turtle.dot()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.dot()
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('kangari')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.write('gituya')
turtle.goto(MIDDLE_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.write('kariua')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELSTAR_Y)
turtle.write('kandara')
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.write('kigumo')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('thika')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('mutheru')
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()
# draw a line frm right to right belstar
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.penup()
# draw line frm left belt star to middle belt star
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELSTAR_Y)
turtle.penup()
# middle to right star
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.penup()
# left belt star to left knee
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()
# draw line frm right belt to right knee
turtle.goto(RIGHT_BELSTAR_X, RIGHT_BELSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.done()
# the above code when represented  as pseudocode
# Set the graphics window size to 500 pixels wide by 600 pixels high
# Draw a dot at (LEFT_SHOULDER_X,
# LEFT_SHOULDER_Y) displays  Left shoulder
# Draw a dot at (RIGHT_SHOULDER_X,
# RIGHT_SHOULDER_Y) displays  Right shoulder
# Draw a dot at (LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  displays Leftmost star in the belt
# Draw a dot at (MIDDLE_BELTSTAR_X,
# MIDDLE_BELTSTAR_Y)  displays  Middle star in the belt
# Draw a dot at (RIGHT_BELTSTAR_X,
# RIGHT_BELTSTAR_Y)  displays Rightmost star in the belt
# Draw a dot at (LEFT_KNEE_X, LEFT_KNEE_Y)  shows Left knee
# Draw a dot at (RIGHT_KNEE_X, RIGHT_KNEE_Y)
