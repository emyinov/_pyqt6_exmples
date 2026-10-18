# Qt6. Widgets. Виджет QLabel.

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QSpinBox, QDoubleSpinBox, QSlider, 
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        # widget.setPixmap(QPixmap("cat.jpg"))
        # widget.setScaledContents(True)

        self.setCentralWidget(widget)
# -----------------------------------------------------------------------------

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()