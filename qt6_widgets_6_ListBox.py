# Qt6. Widgets. Виджет QListWidget.

import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QSpinBox, QDoubleSpinBox, QSlider,
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self,item) : # item - не индекс, а сам QList (элемент списка - объект)
        print(f"ItemChanged event: {index}, {index.text()}")

    def text_changed(self,str) : # str - строка
        print(f"TextChanged event: {str}")

# -----------------------------------------------------------------------------

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()