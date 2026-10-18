# Qt6. Widgets. Виджет ComboBox.

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

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # Сигнал currentIndexChanged срабатывает при обновлении выбранного в
        # данный момент эемента, индекс которого в списке передается по умолчанию
        widget.currentIndexChanged.connect(self.index_changed)

        # Сигнал currentTextChanged также срабатывает при обновлении выбранного в
        # данный момент эемента с передачей метки (текста) выбранного элемета
        widget.currentTextChanged.connect(self.text_changed)

        widget.setEditable(True)
        # widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)

        self.setCentralWidget(widget)

    def index_changed(self,index) : # index - целое число
        print(f"IndexChanged Hndl: new_index -> {index}")

    def text_changed(self,str) : # str - текст (метка элемента списка)
        print(f"TextChanged Hndl: new_text -> {str}")

# -----------------------------------------------------------------------------

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()