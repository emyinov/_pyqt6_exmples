# Qt6. Контекстное меню. Контекстное меню появляется при нажатии правой кнопки мыши.
# 1. Перехват события contextMenuEvent в QMainWindow

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()

    def contextMenuEvent(self, e) :
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())
        # return super().contextMenuEvent(event)

# -----------------------------------------------------------------------------

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()