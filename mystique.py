# import the turtle module and time module for delay
import turtle
from time import sleep

# create a turtle object
t = turtle.Turtle()

# set the speed of the turtle
t.speed(4)

# set the background color of the screen
turtle.bgcolor("white")

# set the color of the turtle
t.color("white")

# set the title of the window
turtle.title('MYSTIQUE Logo')

# move the turtle to the starting position
t.up()
t.goto(-80, 50)
t.down()

# draw the outer box of the logo
t.fillcolor("black")
t.begin_fill()
t.forward(200)
t.setheading(270)
s = 360
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.forward(180)
s = 270
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.forward(200)
s = 180
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.forward(180)
s = 90
for i in range(9):
    s = s - 10
    t.setheading(s)
    t.forward(10)
t.forward(30)
t.end_fill()

# draw the red stripe in the logo
t.up()
t.color("black")
t.setheading(270)
t.forward(240)
t.setheading(0)
t.down()
t.color("red")
t.fillcolor("#E50914")
t.begin_fill()
t.forward(30)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(30)
t.setheading(270)
t.forward(180)
t.end_fill()
t.setheading(0)
t.up()
t.forward(75)
t.down()
t.color("red")
t.fillcolor("#E50914")
t.begin_fill()
t.forward(30)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(30)
t.setheading(270)
t.forward(180)
t.end_fill()

# draw the "M" in the logo
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.setheading(113)
t.forward(195)
t.setheading(0)
t.forward(31)
t.setheading(293)
t.forward(196)
t.setheading(203)
t.forward(196)
t.setheading(0)
t.forward(31)
t.setheading(113)
t.forward(195)
t.end_fill()

# draw the "Y" in the logo
t.up()
t.setheading(293)
t.forward(60)
t.down()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.setheading(240)
t.forward(150)
t.setheading(0)
t.forward(30)
t.setheading(60)
t.forward(150)
t.end_fill()

# draw the "S" in the logo
t.up()
t.setheading(0)
t.forward(75)
t.down()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.circle(35, -90)
t.setheading(270)
t.forward(70)
t.setheading(0)
t.circle(35, -90)
t.end_fill()

# draw the "T" in the logo
t.up()
t.forward(80)
t.down()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.forward(30)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(30)
t.end_fill()

# draw the "I" in the logo
t.up()
t.forward(80)
t.down()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.forward(30)
t.setheading(270)
t.forward(180)
t.setheading(180)
t.forward(30)
t.end_fill()

# draw the "Q" in the logo
t.up()
t.forward(80)
t.down()
t.color("red")
t.fillcolor("red")
t.begin_fill()
t.setheading(270)
t.forward(60)
t.circle(30, 180)
t.forward(60)
t.setheading(180)
t.forward(60)
t.setheading(90)
t.circle(30, 180)
t.forward(60)
t.end_fill()

# hide the turtle and wait for 10 seconds before closing the window
t.hideturtle()
sleep(10)
turtle.done()