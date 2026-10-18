# Второе GUI приложение на Python средствами PyQt6
# Слоты и сигналы
# Подключаем к кнопке QPushButton два слота, принимающих сигнал clicked от нее

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Подкласс QMinWindow для настройки главного окна приложения
class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My PyQt6 App № 2")
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        
        # button.clicked.connect(self.the_button_was_clicked)

        # self.button.clicked.connect(self.the_button_was_toggled)
        
        self.button.released.connect(self.the_button_was_relesed)
        
        self.button.setChecked(self.button_is_checked)
        
        self.setFixedSize(QSize(400,300))
        # Устанавливаем центральный виджет Window
        self.setCentralWidget(self.button)

    # def the_button_was_clicked(self) :
    #     print("Clicked!")

    def the_button_was_toggled(self,checked) :
        # print("Checked?",checked)
        self.button_is_checked = checked
        print("Event: Button clicked, status: ", self.button_is_checked)

    def the_button_was_relesed(self) :
        self.button_is_checked = self.button.isChecked()
        print("Event: Button released, status: ", self.button_is_checked)

# ---------------------------------------------------------------

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()