# Qt6. Widgets. Группа радиокнопок. Использование двух основных подходов:
# 1) QGroupBox - визуальная группировка
# 2) QButtonGroup - логическая группировка

import sys
from PyQt6.QtWidgets import ( QApplication, QWidget, QVBoxLayout, QGroupBox, 
                             QRadioButton, QPushButton, QMessageBox )

class Window(QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 -> RadioButton Group example")

        main_layout = QVBoxLayout()
        # Создание рамки-группы (визуальная группировка)
        self.group_box = QGroupBox("Выберите операционную систему: ")
        vbox = QVBoxLayout()

        self.rb_win = QRadioButton("Windows")
        self.rb_linux = QRadioButton("Linux")
        self.rb_mac = QRadioButton("macOS")
        self.rb_win.setChecked(True) # Выбор по умолчанию

        vbox.addWidget(self.rb_win)
        vbox.addWidget(self.rb_linux)
        vbox.addWidget(self.rb_mac)

        self.group_box.setLayout(vbox)
        main_layout.addWidget(self.group_box)

        # Кнопка проверки выбора
        btn = QPushButton("OK")
        btn.clicked.connect(self.check_selection)
        main_layout.addWidget(btn)

        self.setLayout(main_layout)

    def check_selection(self) :
        choice = "Ничего не выбрано"
        if self.rb_win.isChecked() :
            choice = "Windows"
        elif self.rb_linux.isChecked() :
            choice = "Linux"
        elif self.rb_mac.isChecked() :
            choice = "macOS"

        QMessageBox.information(self, "Выбор", f"Вы выбрали: {choice}")

# -------------------------------------------------------------------------

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())