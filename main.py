Tkinter Example:

import tkinter as tk
from tkinter import ttk
import time

def run_tasks():
    for i in range(10):
        progress_var.set(i * 10)
        root.update()
        time.sleep(1)

root = tk.Tk()
root.title("Task Progress")

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack()

run_button = ttk.Button(root, text="Run Tasks", command=run_tasks)
run_button.pack()

root.mainloop()

Matplotlib Example:

import matplotlib.pyplot as plt
import numpy as np
import time

def run_tasks():
    for i in range(10):
        progress_bar.set_val(i * 10)
        plt.pause(1)
        progress_bar.ax.figure.canvas.draw()

fig, ax = plt.subplots()
progress_bar = plt.ProgressBar(ax, 'Tasks', 0, 100)
ax.add_artist(progress_bar)

run_button = plt.Button(fig, 'Run Tasks', run_tasks)
run_button.on_clicked(run_tasks)

plt.show()

Flask Web-based Dashboard Example:

from flask import Flask, render_template
import time
import threading

app = Flask(__name__)

progress = 0

def simulate_tasks():
    global progress
    for i in range(10):
        progress = i * 10
        time.sleep(1)

@app.route('/')
def index():
    return render_template('dashboard.html', progress=progress)

if __name__ == '__main__':
    threading.Thread(target=simulate_tasks).start()
    app.run()

For the web-based dashboard example, you’ll need to create an HTML template (dashboard.html) to display the progress using Flask’s render_template function.

These are simplified examples to get you started with each approach. Depending on your actual requirements, you may need to customize and expand upon these examples to fit your specific use case.


Certainly! Here are the remaining examples for creating a GUI with PyQt, Kivy, and a web-based dashboard using Django:

PyQt Example:

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QTimer
import time

class TaskRunner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Progress")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.run_button = QPushButton("Run Tasks")
        self.layout.addWidget(self.run_button)

        self.run_button.clicked.connect(self.run_tasks)

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.counter = 0

    def run_tasks(self):
        self.counter = 0
        self.timer.start(1000)

    def update_progress(self):
        self.counter += 10
        self.progress_bar.setValue(self.counter)
        if self.counter >= 100:
            self.timer.stop()

def main():
    app = QApplication(sys.argv)
    window = TaskRunner()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

Kivy Example:

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
import time

class TaskRunner(BoxLayout):
    def __init__(self):
        super().__init__(orientation='vertical')
        self.progress_bar = ProgressBar(max=10)
        self.add_widget(self.progress_bar)
        self.run_button = Button(text="Run Tasks")
        self.run_button.bind(on_press=self.run_tasks)
        self.add_widget(self.run_button)

    def run_tasks(self, instance):
        for i in range(10):
            self.progress_bar.value = (i + 1)
            time.sleep(1)

class MyApp(App):
    def build(self):
        return TaskRunner()

if __name__ == '__main__':
    MyApp().run()
