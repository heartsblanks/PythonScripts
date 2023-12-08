from turtle import *
import time

bgcolor('grey')
right(90)

pos = [-40, 40]
for x, y in zip(pos, pos):
    up()
    goto(x, y)
    down()
    fillcolor('red')
    begin_fill()
    for _ in range(2):
        forward(200)
        right(90)
        forward(40)
        right(90)
    end_fill()

time.sleep(2)
bgcolor('black')
time.sleep(2)