import turtle
import tkinter as tk

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

# Create Tkinter window
root = tk.Tk()
root.title("MYSTIQUE Intro")

# Create a frame
frame = tk.Frame(root, bg="black")
frame.pack(expand=True, fill="both")

# Create a Canvas widget for turtle graphics
canvas = tk.Canvas(frame, bg="black", width=400, height=200)
canvas.pack()

# Create a turtle
mystique_turtle = turtle.RawTurtle(canvas)
mystique_turtle.speed(2)
mystique_turtle.color("white")
mystique_turtle.penup()
mystique_turtle.hideturtle()

# Draw MYSTIQUE on canvas
draw_mystique()

# Close the turtle graphics window on click
root.mainloop()