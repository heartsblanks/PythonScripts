from turtle import *
import time

bgcolor('grey')
right(90)

# Define positions for each letter
positions = [-40, 40, 120, 200, 280, 360]

for x in positions:
    up()
    goto(x, 0)
    down()
    fillcolor('red')
    begin_fill()
    
    # Draw the letter
    if x != 200:  # For letters other than 'T'
        for _ in range(2):
            forward(200)
            left(90)
            forward(40)
            left(90)
    else:  # For 'T'
        left(22)
        for _ in range(2):
            forward(217)
            left(68)
            forward(40)
            left(112)
    
    end_fill()

# Delay before changing background color
time.sleep(2)
bgcolor('black')
time.sleep(2)