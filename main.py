import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class PipelineVisualization(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 400)
        self.setWindowTitle('Jenkins-like Pipeline Visualization')

        scene = QGraphicsScene(self)
        view = QGraphicsView(scene, self)
        view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        view.setSceneRect(0, 0, 800, 400)

        stages = [("Stage 1", 30), ("Stage 2", 60), ("Stage 3", 80)]

        x = 50
        y = 150
        width = 100
        height = 100

        for stage, progress in stages:
            item = QGraphicsRectItem(x, y, width, height)
            item.setBrush(QColor(173, 216, 230))  # Light Blue
            scene.addItem(item)

            progress_item = QGraphicsRectItem(x, y + height - 10, (width * progress) / 100, 10)
            progress_item.setBrush(QColor(0, 128, 0))  # Green
            scene.addItem(progress_item)

            scene.addText(stage).setPos(x + width / 2 - 20, y - 20)

            x += width + 50

        self.setCentralWidget(view)

def main():
    app = QApplication(sys.argv)
    ex = PipelineVisualization()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()