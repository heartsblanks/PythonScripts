import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Pipeline Progress Visualization")

# Create a canvas widget to draw the pipeline
canvas = tk.Canvas(window, width=800, height=400)
canvas.pack()

# Define the stages in the pipeline
stages = ["Stage 1", "Stage 2", "Stage 3", "Stage 4", "Stage 5"]

# Define the width and height of each stage box
stage_width = 100
stage_height = 50

# Define the spacing between stages
spacing = 20

# Define the progress for each stage (as a percentage)
stage_progress = [20, 40, 60, 80, 100]

# Calculate the total width of the pipeline
total_width = len(stages) * (stage_width + spacing) - spacing

# Draw the stages as rectangular boxes with progress bars
for i, (stage, progress) in enumerate(zip(stages, stage_progress)):
    x1 = (i * (stage_width + spacing)) + spacing  # Calculate x-coordinate of the stage box
    y1 = 150  # Set a fixed y-coordinate for all stages
    x2 = x1 + stage_width  # Calculate the x-coordinate of the right edge of the stage box
    y2 = y1 + stage_height  # Calculate the y-coordinate of the bottom edge of the stage box
    
    # Draw the stage box
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=stage)
    
    # Draw the progress bar
    progress_x2 = x1 + (stage_width * progress / 100)
    canvas.create_rectangle(x1, y1, progress_x2, y2, fill="green")

# Run the Tkinter main loop
window.mainloop()