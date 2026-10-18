# Qt6. События. Пример обработки события QMouseEvent виджетом QLabel.

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        
        self.setMouseTracking(True) # Отслеживание мыши для QMainWindow (window)
        self.label.setMouseTracking(True) # Отслеживание мыши для виджета QLabel (label) 

    def mouseMoveEvent(self, e) :
        self.label.setText("mouseMoveEvent")
        # return super().mouseMoveEvent(e)

    def mousePressEvent(self, e) :
        # self.label.setText("mousePressEvent")
        if e.button() == Qt.MouseButton.LeftButton :
            self.label.setText("mousePressEvent LEFT")
        
        elif e.button() == Qt.MouseButton.MiddleButton :
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton :
                    self.label.setText("mousePressEvent RIGHT")
        # return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e) :
        # self.label.setText("mouseReleaseEvent")
        if e.button() == Qt.MouseButton.LeftButton :
            self.label.setText("mouseReleaseEvent LEFT")
        
        elif e.button() == Qt.MouseButton.MiddleButton :
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton :
                    self.label.setText("mouseReleaseEvent RIGHT")
        # return super().mouseReleaseEvent(e)

    def mouseDoubleClickEvent(self, e) :
        # self.label.setText("mouseDoubleClickEvent")
        if e.button() == Qt.MouseButton.LeftButton :
            self.label.setText("mouseDoubleClickEvent LEFT")
        
        elif e.button() == Qt.MouseButton.MiddleButton :
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton :
                    self.label.setText("mouseDoubleClickEvent RIGHT")

        # return super().mouseDoubleClickEvent(e)
# --------------------------------------------------------------------------

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()