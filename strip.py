import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(2)  # Set the drawing speed (1=slowest, 10=fastest)

# Function to draw a striping circle
def striping_circle(radius, stripes, color1, color2):
    for _ in range(stripes):
        t.color(color1 if _ % 2 == 0 else color2)
        t.fillcolor('blue')
        t.circle(radius)
        t.right(360 / stripes)

# Draw a series of striping circles
for i in range(5):  # Draw 5 circles
    striping_circle(50 + i * 20, 12, "red", "white")
    t.penup()
    t.forward(40)  # Move turtle forward for the next circle
    t.pendown()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
