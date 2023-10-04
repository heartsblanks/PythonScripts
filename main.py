import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from PyQt5.QtGui import QColor, QBrush, QPen, qDegreesToRadians, qCos, qSin
from PyQt5.QtCore import Qt, QPointF, QLineF

# Rest of the code remains the same...
class StageItem(QGraphicsRectItem):
    def __init__(self, name, x, y, width, height):
        super().__init__(x, y, width, height)
        self.name = name
        self.setBrush(QBrush(Qt.gray))
        self.setPen(QPen(Qt.black))
        self.successful = False

    def set_success(self, success):
        self.successful = success
        self.setBrush(QBrush(Qt.green if success else Qt.red))

def draw_arrow(scene, start_item, end_item):
    start_center = start_item.rect().center()
    end_center = end_item.rect().center()

    line = QLineF(start_center, end_center)
    angle = line.angle()

    arrow_size = 10  # Size of the arrowhead
    arrow_angle = 30  # Angle of the arrowhead

    # Calculate rotated arrow points
    arrow_p1 = end_center + QPointF(
        arrow_size * qCos(qDegreesToRadians(angle - arrow_angle)),
        arrow_size * qSin(qDegreesToRadians(angle - arrow_angle))
    )
    
    arrow_p2 = end_center + QPointF(
        arrow_size * qCos(qDegreesToRadians(angle + arrow_angle)),
        arrow_size * qSin(qDegreesToRadians(angle + arrow_angle))
    )

    arrow_head = scene.addPolygon([end_center, arrow_p1, arrow_p2])
    arrow_line = scene.addLine(line)

    arrow_head.setBrush(QBrush(Qt.black))
    arrow_line.setPen(QPen(Qt.black))
    
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

    # Draw arrows connecting stages
    draw_arrow(scene, stages[0], stages[1])
    # Add more arrows as needed

    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()