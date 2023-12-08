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

# Function to draw MYSTIQUE
def draw_mystique():
    mystique_turtle.goto(-100, 0)
    mystique_turtle.pendown()
    mystique_turtle.write("M", font=("Arial", 36, "bold"))
    mystique_turtle.penup()
    mystique_turtle.goto(-50, 0)
    mystique_turtle.pendown()
    mystique_turtle.write("Y", font=("Arial", 36, "bold"))
    mystique_turtle.penup()
    mystique_turtle.goto(0, 0)
    mystique_turtle.pendown()
    mystique_turtle.write("S", font=("Arial", 36, "bold"))
    mystique_turtle.penup()
    mystique_turtle.goto(50, 0)
    mystique_turtle.pendown()
    mystique_turtle.write("T", font=("Arial", 36, "bold"))
    mystique_turtle.penup()
    mystique_turtle.goto(100, 0)
    mystique_turtle.pendown()
    mystique_turtle.write("I", font=("Arial", 36, "bold"))
    mystique_turtle.penup()
    mystique_turtle.goto(150, 0)
    mystique_turtle.pendown()
    mystique_turtle.write("Q", font=("Arial", 36, "bold"))
    mystique_turtle.penup()

# Draw the MYSTIQUE animation
draw_mystique()

# Close the turtle graphics window on click
screen.exitonclick()