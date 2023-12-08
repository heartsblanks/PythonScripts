from turtle import *
import time

bgcolor('grey')
speed(2)
width(5)

up()
goto(-40, 40)
down()

fillcolor('red')
begin_fill()

# Draw the letter "N"
forward(200)
right(150)
forward(220)
left(150)
forward(200)

end_fill()

time.sleep(2)
bgcolor('black')
time.sleep(2)