import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt5.QtGui import QColor, QBrush, QPen
from PyQt5.QtCore import Qt, QPointF, QLineF

class StageItem(QGraphicsRectItem):
    def __init__(self, name, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = name
        self.setBrush(QBrush(Qt.gray))
        self.setPen(QPen(Qt.black))
        self.successful = False
        self.progress = 0  # Initialize progress to 0

    def set_success(self, success):
        self.successful = success
        self.setBrush(QBrush(Qt.green if success else Qt.red))

    def set_progress(self, progress):
        self.progress = progress
        self.update()  # Call update to redraw the stage with updated progress

    def paint(self, painter, option, widget=None):
        super().paint(painter, option, widget)
        # Draw a progress bar within the stage
        progress_rect = self.rect()
        progress_rect.setWidth(self.progress * self.rect().width() / 100)  # Adjust width based on progress
        painter.fillRect(progress_rect, QBrush(Qt.green))

def draw_arrow(scene, start_item, end_item):
    # Rest of the code remains the same...

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    scene = QGraphicsScene()
    view = QGraphicsView(scene)

    stages = [
        StageItem("Stage 1", 10, 10, 100, 50),
        StageItem("Stage 2", 150, 10, 100, 50),
        # Add more stages as needed
    ]

    for stage in stages:
        scene.addItem(stage)

    # Simulate success/failure of stages
    stages[0].set_success(True)
    stages[1].set_success(False)

    # Update progress for demonstration (you can replace this with your actual progress updates)
    stages[0].set_progress(30)
    stages[1].set_progress(70)

    # Draw arrows connecting stages
    draw_arrow(scene, stages[0], stages[1])
    # Add more arrows as needed

    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()