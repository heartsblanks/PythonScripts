import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("MYSTIQUE Intro")

# Create a turtle
mystique_turtle = turtle.Turtle()
mystique_turtle.speed(2)
mystique_turtle.color("white")
mystique_turtle.pensize(3)
mystique_turtle.penup()
mystique_turtle.hideturtle()

# Function to draw appealing MYSTIQUE intro
def draw_mystique_appealing_intro():
    draw_appealing_letter("M", -80, 0, mystique_turtle)
    draw_appealing_letter("Y", -20, 0, mystique_turtle)
    draw_appealing_letter("S", 40, 0, mystique_turtle)
    draw_appealing_letter("T", 100, 0, mystique_turtle)
    draw_appealing_letter("I", 160, 0, mystique_turtle)
    draw_appealing_letter("Q", 220, 0, mystique_turtle)

# Function to draw appealing letters
def draw_appealing_letter(letter, x, y, t):
    t.penup()
    t.goto(x, y)
    t.pendown()

    if letter == "M":
        t.left(90)
        t.forward(80)
        t.right(135)
        t.forward(40)
        t.left(135)
        t.forward(40)
        t.right(135)
        t.forward(80)

    elif letter == "Y":
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.backward(80)

    elif letter == "S":
        t.circle(40, -90)
        t.right(90)
        t.circle(40, -90)

    elif letter == "T":
        t.forward(40)
        t.backward(80)
        t.left(90)
        t.forward(40)

    elif letter == "I":
        t.forward(80)
        t.backward(40)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(80)

    elif letter == "Q":
        t.left(90)
        t.forward(80)
        t.right(90)
        t.circle(40, -180)
        t.left(90)
        t.forward(80)

# Draw the appealing MYSTIQUE intro
draw_mystique_appealing_intro()

# Close the turtle graphics window on click
screen.exitonclick()