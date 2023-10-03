import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QProgressBar, QWidget
from PySide6.QtCore import QTimer
import time

class TaskRunner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Progress")
        self.setGeometry(100, 100, 400, 200)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.run_button = QPushButton("Run Tasks")
        layout.addWidget(self.run_button)

        self.run_button.clicked.connect(self.run_tasks)

        central_widget.setLayout(layout)

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