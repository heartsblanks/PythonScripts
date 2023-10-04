import sys
import time
import multiprocessing
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton
from PyQt5.QtCore import QObject, pyqtSignal

class ProgressUpdater(QObject):
    progress_updated = pyqtSignal(int)

    def update_progress(self, value):
        self.progress_updated.emit(value)

def stage1(progress_updater):
    for i in range(101):
        time.sleep(0.05)
        progress_updater.update_progress(i)

def stage2(progress_updater):
    for i in range(101):
        time.sleep(0.03)
        progress_updater.update_progress(i)

def run_pipeline(progress_updater):
    pool = multiprocessing.Pool(processes=2)
    results = pool.map_async(stage1, [progress_updater])
    results.get()
    results = pool.map_async(stage2, [progress_updater])
    results.get()

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(100, 100, 400, 200)

    progress_bar = QProgressBar(window)
    progress_bar.setGeometry(50, 50, 300, 30)

    start_button = QPushButton("Start Pipeline", window)
    start_button.setGeometry(150, 100, 100, 30)

    progress_updater = ProgressUpdater()
    progress_updater.progress_updated.connect(progress_bar.setValue)

    start_button.clicked.connect(lambda: run_pipeline(progress_updater))

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()