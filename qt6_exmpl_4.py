# Четвертое GUI приложение на Python средствами PyQt6
# Слоты и сигналы
# 1. Подключаем к кнопке QPushButton один слот, принимающий сигнал clicked от нее
#    При нажатии на кнопку случайным образом изменяется заголовок окна приложения из
#    заданного списка window_titles. 
# 2. Подключаем сигнал windowTitleChanged в QMainWindow к пользовательскому методу
#    слота. Данный сигнал срабатывает только в случае отличия старого и нового 
#    заголовков 

# from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()

        self.n_times_clicked = 0
        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        # Устанавливаем центральный виджет Window
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self) :
        self.n_times_clicked += 1
        print(f"Event: PushButton clicked {self.n_times_clicked} times")
        new_window_title = choice(window_titles)
        print("Setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title) :
        print("Event: WindowTitleChanged, new title: %s" % window_title)
        
        if window_title == 'Something went wrong' :
            self.button.setDisabled(True)

# -------------------------------------------------------------------------

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()