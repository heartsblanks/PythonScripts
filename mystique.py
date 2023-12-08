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

# Function to draw MYSTIQUE line-style intro
def draw_mystique_line_intro():
    positions = [(-100, 0), (-50, 0), (0, 0), (50, 0), (100, 0), (150, 0)]

    for position in positions:
        mystique_turtle.goto(position)
        mystique_turtle.pendown()
        mystique_turtle.forward(30)  # Draw a line for each letter
        mystique_turtle.penup()

# Draw the MYSTIQUE line-style intro
draw_mystique_line_intro()

# Close the turtle graphics window on click
screen.exitonclick()