# Третье GUI приложение на Python средствами PyQt6
# Слоты и сигналы
# Подключаем к кнопке QPushButton один слот, принимающий сигнал clicked от нее
# При нажатии на кнопку изменяется ее текст и она становится недоступной. Кроме
# того изменяем заголовок окна 

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Подкласс QMinWindow для настройки главного окна приложения
class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()

        # self.button_is_checked = True

        self.setWindowTitle("My PyQt6 App № 3")
        
        self.button = QPushButton("Press Me!")
        # self.button.setCheckable(True)
        
        self.button.clicked.connect(self.the_button_was_clicked)

        # self.button.setChecked(self.button_is_checked)
        
        # self.setFixedSize(QSize(400,300))
        # Устанавливаем центральный виджет Window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self) :
        print("Event: Button clicked")
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        # Также меняем заголовок окна.
        self.setWindowTitle("My Oneshot App")


# ---------------------------------------------------------------

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()