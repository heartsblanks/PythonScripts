import sys
import time
import multiprocessing
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton

def stage1(progress_bar):
    for i in range(101):
        time.sleep(0.05)
        progress_bar.setValue(i)

def stage2(progress_bar):
    for i in range(101):
        time.sleep(0.03)
        progress_bar.setValue(i)

def run_pipeline(progress_bar):
    # Create a multiprocessing pool
    pool = multiprocessing.Pool(processes=2)

    # Execute stages in parallel
    results = pool.map_async(stage1, [progress_bar])
    results.get()
    results = pool.map_async(stage2, [progress_bar])
    results.get()

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(100, 100, 400, 200)

    progress_bar = QProgressBar(window)
    progress_bar.setGeometry(50, 50, 300, 30)

    start_button = QPushButton("Start Pipeline", window)
    start_button.setGeometry(150, 100, 100, 30)
    start_button.clicked.connect(lambda: run_pipeline(progress_bar))

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()