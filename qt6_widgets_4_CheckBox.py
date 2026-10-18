# Qt6. Widgets. Виджет QCheckBox.

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

        widget = QCheckBox("This is a checkbox")
        widget.setCheckState(Qt.CheckState.Checked)

        # Включение трех состояний: widget.setCheckState(Qt.PartiallyChecked)
        # Или: widget.setTriState(True)
        widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s) :
        print(f"Qt.CheckState.Checked: {Qt.CheckState.Checked.value}")
        print(s == Qt.CheckState.Checked.value)
        print(s," -> ",Qt.CheckState(s))

# -----------------------------------------------------------------------------

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()