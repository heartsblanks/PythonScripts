import subprocess
import tkinter as tk

def run_maven_command():
    # Replace 'your_maven_command' with your actual Maven command
    maven_command = 'your_maven_command'
    
    # Create a new subprocess and open a pipe to its standard output
    process = subprocess.Popen(maven_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Maven Command Output")
    
    # Create a Text widget to display the command output with monospaced font
    output_text = tk.Text(window, wrap=tk.WORD, font=("Courier New", 10))
    output_text.pack()
    
    # Configure background and foreground colors
    output_text.config(bg="black", fg="white")
    
    # Create a function to update the Text widget in real-time
    def update_output():
        line = process.stdout.readline()
        if line:
            output_text.insert(tk.END, line)
            output_text.see(tk.END)  # Auto-scroll to the end of the Text widget
            window.after(10, update_output)  # Schedule the function to run again
        else:
            # Command has finished, disable the button
            run_button.config(state=tk.DISABLED)
            
            # Wait for the process to complete and get the exit code
            process.wait()
            return_code = process.returncode
            
            if return_code == 0:
                window.destroy()  # Close the window if the command was successful

    # Create a button to trigger the Maven command
    run_button = tk.Button(window, text="Run Maven Command", command=update_output)
    run_button.pack()
    
    update_output()  # Start the real-time update
    
    window.mainloop()

# Run the Maven command when the script starts
run_maven_command()