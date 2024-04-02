
import turtle

# Function to draw a square
def draw_square(turtle, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

# Function to draw a 3D cube
def draw_cube(turtle, x, y, size):
    # Draw front square
    draw_square(turtle, x, y, size)

    # Draw back square
    draw_square(turtle, x - size * 0.5, y - size * 0.5, size)

    # Connect front and back squares
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x - size * 0.5, y - size * 0.5)
    turtle.penup()
    turtle.goto(x + size, y)
    turtle.pendown()
    turtle.goto(x + size * 0.5, y - size * 0.5)

    # Draw top lines
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.goto(x - size * 0.5, y - size * 0.5)
    turtle.penup()
    turtle.goto(x + size, y)
    turtle.pendown()
    turtle.goto(x + size * 0.5, y - size * 0.5)

# Initialize screen and turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.setworldcoordinates(-300, -300, 300, 300)

t = turtle.Turtle()
t.speed(0)

# Draw a 3D cube
draw_cube(t, 0, 0, 100)

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()


