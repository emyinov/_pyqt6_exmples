# Qt6. Widgets. Группа радиокнопок. Использование двух основных подходов:
# 1) QGroupBox - визуальная группировка
# 2) QButtonGroup - логическая группировка

import sys
from PyQt6.QtWidgets import ( QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QRadioButton, QButtonGroup, QLabel, QGroupBox )

class Window(QWidget) :
    def __init__(self) :
        super().__init__()
        self.init_ui()
        self.update_status()

    def init_ui(self) :
        
        self.setWindowTitle("PyQt6 -> QRadioButton & QButtonGroup")
        self.resize(400,250)

        # Главный вертикальный слой
        main_layout = QVBoxLayout()
        # Горизонтальный слой для размещения двух колонок (групп) рядом
        columns_layout = QHBoxLayout()


        # -------------------------- ГРУППА 1: ОС ------------------------------
        # Создание рамки-группы (визуальная группировка)
        os_box = QGroupBox("Выберите ОС: ")
        os_layout = QVBoxLayout()

        # Создаем ПЕРВУЮ ЛОГИЧЕСКУЮ группу
        self.os_group = QButtonGroup(self)
        
        # Создаем кнопки
        rb_windows = QRadioButton("Windows")
        rb_linux = QRadioButton("Linux")
        rb_macos = QRadioButton("macOS")

        #Добавляеи кнопки в логическую группу (с назначением ID) 
        self.os_group.addButton(rb_windows,1)
        self.os_group.addButton(rb_linux,2)
        self.os_group.addButton(rb_macos,3)

        # Добавляем кнопки на визуальный слой
        os_layout.addWidget(rb_windows)
        os_layout.addWidget(rb_linux)
        os_layout.addWidget(rb_macos)
        os_box.setLayout(os_layout)

        # ----------------------------- ГРУППА 2: ТЕМА -------------------------
        theme_box = QGroupBox("Выберите тему:")
        theme_layout = QVBoxLayout()

        # Создаем ВТОРУЮ ЛОГИЧЕСКУЮ группу
        self.theme_group = QButtonGroup(self)

        # Создаем кнопки
        rb_light = QRadioButton("Светлая")
        rb_dark = QRadioButton("Темная")

        # Добавляем кнопки во вторую группу
        self.theme_group.addButton(rb_light, 10)
        self.theme_group.addButton(rb_dark, 20)

        # Добавляем кнопки на визуальный слой
        theme_layout.addWidget(rb_light)
        theme_layout.addWidget(rb_dark)
        theme_box.setLayout(theme_layout)
        
        # ------------------------ ОБРАБОТКА СИГНАЛОВ --------------------------
        # Сигнал idClicked отправляет ID нажатой кнопки (удобно для условий)
        self.os_group.idClicked.connect(self.update_status)
        self.theme_group.idClicked.connect(self.update_status)

        # Текстовая метка для вывода результата
        self.status_label = QLabel("Сделайте Ваш выбор")

        # Собираем интерфейс вместе
        columns_layout.addWidget(os_box)
        columns_layout.addWidget(theme_box)

        # -------------------- ГРУППА 3: ПРОИЗВОДИТЕЛЬНОСТЬ --------------------
        gr3_layout = QVBoxLayout()

        self.perform_box = QGroupBox("Режим производительности")
        self.perform_box.setCheckable(True) # Кликабельный QGroupBox
        self.perform_box.setChecked(False)  # По умолчанию выключен
        # Внутренний слой для элементов внутри группы perform_box
        perform_layout = QVBoxLayout()
        # Создаем радиокнопки
        self.rb_perform_high = QRadioButton("Высокая")
        self.rb_perform_optimal = QRadioButton("Оптимальная")
        self.rb_perform_economy = QRadioButton("Экономная")

        # Добавляем кнопки на визуальный слой perform_layout
        perform_layout.addWidget(self.rb_perform_high)
        perform_layout.addWidget(self.rb_perform_optimal)
        perform_layout.addWidget(self.rb_perform_economy)
        
        self.perform_box.setLayout(perform_layout)
        
        # perform_layout.addWidget(self.perform_box)

        # Текстовая метка для вывода режима производительности
        self.perform_label = QLabel("Режим производительности")

        # Собираем интерфейс группы 3 вместе
        gr3_layout.addWidget(self.perform_box)
        gr3_layout.addWidget(self.perform_label)        

        # ПОДКЛЮЧЕНИЕ СИГНАЛОВ к perform_box
        # Сигнал toggled реагирует на любые изменения состояния: пользователя либо программы
        self.perform_box.toggled.connect(self.on_perform_box_toggled)
        
        # Обработка сигнала toggled для всех радиокнопок perform_box
        self.rb_perform_high.toggled.connect(self.on_rb_perform_toggled)
        self.rb_perform_optimal.toggled.connect(self.on_rb_perform_toggled)
        self.rb_perform_economy.toggled.connect(self.on_rb_perform_toggled)


        main_layout.addLayout(columns_layout)
        main_layout.addWidget(self.status_label)

        main_layout.addLayout(gr3_layout)
        # main_layout.addWidget(self.perform_box)
        # main_layout.addLayout(perform_layout)

        # main_layout.addWidget(self.perform_label)

        
        self.setLayout(main_layout)

    def update_status(self) :
        # Способ 1: Получаем текст через checkedButton()
        sel_os_btn = self.os_group.checkedButton()
        os_text = sel_os_btn.text() if sel_os_btn else "Не выбрано"

        # Способ 2: Получаем ID через checkedId()
        theme_id = self.theme_group.checkedId()
        theme_text = "Не выбрано"
        if theme_id == 10 :
            theme_text = "Светлая"
        elif theme_id == 20 :
            theme_text = "Темная"

        # Обновляем текст на экране
        self.status_label.setText(f"ОС: {os_text} | Тема: {theme_text}")

    def on_perform_box_toggled(self, is_checked) :
        """Срабатывает всегда при изменении состояния пользователем или программой """
        msg = "Настройки производительности: "
        if is_checked :
            msg += "ВКЛЮЧЕНЫ"
            # self.perform_label.setText("Настройки производительности: ВКЛЮЧЕНЫ")
        else :
            msg += "ВЫКЛЮЧЕНЫ"
            # self.perform_label.setText("Настройки производительности: ВЫКЛЮЧЕНЫ")
        # Выключение всех радиокнопок режима производительности при изменении состояния
        rd_btns_perform = self.perform_box.findChildren(QRadioButton)
        perform_mode = "\nРежим производительности НЕ ЗАДАН."
        for rb in rd_btns_perform :
            if rb.isChecked() :
                perform_mode = f"\nРанее выбранный режим: {rb.text().upper()}"
                rb.setAutoExclusive(False)
                rb.setChecked(False)
                rb.setAutoExclusive(True)

        msg += perform_mode
        self.perform_label.setText(msg)

    def on_rb_perform_toggled(self) :
        """Срабатывает при изменении состояния радиокнопки в группе perform_box"""
        sender = self.sender()
        
        if isinstance(sender,QRadioButton) and sender.isChecked() :
            msg = "Настройки производительности: "
            if self.perform_box.isChecked() :
                msg += "ВКЛЮЧЕНЫ"
            else :
                msg += "ВЫКЛЮЧЕНЫ"
            perform_mode = f"\nПроизводительность изменена на: {sender.text().upper()}"
            msg += perform_mode
            self.perform_label.setText(msg)

        


        
    #     # Кнопка проверки выбора
    #     btn = QPushButton("OK")
    #     btn.clicked.connect(self.check_selection)
    #     main_layout.addWidget(btn)

    #     self.setLayout(main_layout)

    # def check_selection(self) :
    #     choice = "Ничего не выбрано"
    #     if self.rb_win.isChecked() :
    #         choice = "Windows"
    #     elif self.rb_linux.isChecked() :
    #         choice = "Linux"
    #     elif self.rb_mac.isChecked() :
    #         choice = "macOS"

    #     QMessageBox.information(self, "Выбор", f"Вы выбрали: {choice}")

# -------------------------------------------------------------------------

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())