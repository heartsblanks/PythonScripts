from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QPropertyAnimation

class MystiqueIntro(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.label = QLabel("Welcome to the Mystique Experience!", self)
        layout.addWidget(self.label)

        self.setGeometry(100, 100, 800, 600)
        self.show()

        self.animate_intro()

    def animate_intro(self):
        animation = QPropertyAnimation(self.label, b"geometry")
        animation.setDuration(3000)
        animation.setStartValue(self.label.geometry())
        animation.setEndValue(self.label.geometry().adjusted(0, 100, 0, 100))
        animation.setEasingCurve(Qt.CurveType.InOutQuart)
        animation.start()

if __name__ == "__main__":
    app = QApplication([])
    window = MystiqueIntro()
    app.exec_()