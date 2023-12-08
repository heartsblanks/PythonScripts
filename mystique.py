import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("MYSTIQUE Intro")

# Create a turtle
mystique_turtle = turtle.Turtle()
mystique_turtle.speed(2)
mystique_turtle.color("white")
mystique_turtle.penup()
mystique_turtle.hideturtle()

# Function to draw MYSTIQUE Netflix-style intro
def draw_mystique_netflix_intro():
    mystique_turtle.goto(-80, 0)
    mystique_turtle.pendown()
    mystique_turtle.circle(50, 180)  # Draw curved part of 'M'

    mystique_turtle.penup()
    mystique_turtle.goto(-30, 0)
    mystique_turtle.pendown()
    mystique_turtle.right(180)
    mystique_turtle.circle(50, -180)  # Draw other curved part of 'M'

    mystique_turtle.penup()
    mystique_turtle.goto(20, 0)
    mystique_turtle.pendown()
    mystique_turtle.forward(40)  # Draw vertical line for 'Y'

    mystique_turtle.penup()
    mystique_turtle.goto(70, 0)
    mystique_turtle.pendown()
    mystique_turtle.circle(50, 180)  # Draw curved part of 'S'

    mystique_turtle.penup()
    mystique_turtle.goto(120, -40)
    mystique_turtle.pendown()
    mystique_turtle.right(90)
    mystique_turtle.forward(80)  # Draw horizontal line for 'S'

    mystique_turtle.penup()
    mystique_turtle.goto(70, -80)
    mystique_turtle.pendown()
    mystique_turtle.circle(50, -180)  # Draw other curved part of 'S'

    mystique_turtle.penup()
    mystique_turtle.goto(170, 0)
    mystique_turtle.pendown()
    mystique_turtle.forward(40)  # Draw vertical line for 'T'

    mystique_turtle.penup()
    mystique_turtle.goto(220, 0)
    mystique_turtle.pendown()
    mystique_turtle.circle(20, 180)  # Draw curved part of 'I'

    mystique_turtle.penup()
    mystique_turtle.goto(240, 0)
    mystique_turtle.pendown()
    mystique_turtle.forward(40)  # Draw horizontal line for 'I'

    mystique_turtle.penup()
    mystique_turtle.goto(260, 0)
    mystique_turtle.pendown()
    mystique_turtle.circle(20, -180)  # Draw other curved part of 'I'

    mystique_turtle.penup()
    mystique_turtle.goto(320, 0)
    mystique_turtle.pendown()
    mystique_turtle.circle(50, 180)  # Draw curved part of 'Q'

    mystique_turtle.penup()
    mystique_turtle.goto(370, -40)
    mystique_turtle.pendown()
    mystique_turtle.right(90)
    mystique_turtle.forward(80)  # Draw horizontal line for 'Q'

    mystique_turtle.penup()
    mystique_turtle.goto(320, -80)
    mystique_turtle.pendown()
    mystique_turtle.circle(50, -180)  # Draw other curved part of 'Q'

# Draw the MYSTIQUE Netflix-style intro
draw_mystique_netflix_intro()

# Close the turtle graphics window on click
screen.exitonclick()