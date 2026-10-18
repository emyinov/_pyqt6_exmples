# Qt6. Widgets. Виджет QListWidget. Демонстрация основных операций со списком:
# добавление, удаление, сортировка элементов списка, получение выбранного значения
# и обработка двойного клика.

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QLineEdit, QMessageBox,
)
from PyQt6.QtCore import Qt

class ListWidgetAdvancedExample(QWidget) :
    def __init__(self) :
        super().__init__()
        self.init_ui()

    def init_ui(self) :
        self.setWindowTitle("PyQt6 example -> QListWidget")
        self.resize(500,400)

        main_layout = QVBoxLayout()
        # 1. Создаем экземпляр класса QListWidget и сохраняем в self, так как
        # он нужен во всех методах
        self.wg_list = QListWidget()
        # Настройка режима выбора элементов списка: разрешаем выбирать несколько
        # элементов через Ctrl/Shift
        self.wg_list.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)

        # 2. Заполнение списка исходными данными
        self.wg_list.addItems(["Apple", "Banana", "Orange", "Grapes", ])

        # 3. Подключение сигналов
        # 3.1 Одиночный клик
        self.wg_list.itemClicked.connect(self.on_item_clicked)
        # 3.2 Двойной клик
        self.wg_list.itemDoubleClicked.connect(self.on_item_double_clicked)

        # Создаем экземпляр класса QLineEdit() для добавления новых элементов
        self.wg_lineedit = QLineEdit()
        self.wg_lineedit.setPlaceholderText("Input fruit name ...")

        # Кнопки управления (локальные переменные, т.к. вне init_ui они не используются)
        btn_layout = QHBoxLayout()
        btn_add = QPushButton("Добавить")
        btn_remove = QPushButton("Удалить выбранные")
        btn_sort = QPushButton("Сортировать")
        btn_clear = QPushButton("Очистить все")

        # Подключаем кнопки к методам
        btn_add.clicked.connect(self.add_new_item)
        btn_remove.clicked.connect(self.remove_selected_items)
        btn_sort.clicked.connect(self.sort_items)
        btn_clear.clicked.connect(self.wg_list.clear)

        btn_layout.addWidget(btn_add)
        btn_layout.addWidget(btn_remove)
        btn_layout.addWidget(btn_sort)
        btn_layout.addWidget(btn_clear)

        # Сборка интерфейса
        main_layout.addWidget(self.wg_list)
        main_layout.addWidget(self.wg_lineedit)
        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

    def on_item_clicked(self, item : QListWidgetItem) :
        """Срабатывает при клике на элементе списка. Принимает объект элемента списка. """
        print(f"Клик на элементе списка: {item.text()}")

    def on_item_double_clicked(self, item : QListWidgetItem) :
        """Срабатывает при двойном клике."""
        QMessageBox.information(self,"Информация", 
                                f"Двойной клик на элементе списка: {item.text()}")

    def add_new_item(self) :
        """Добавление элемента с кастомизацией через QListWidgetItem."""
        text = self.wg_lineedit.text().strip()
        if text :
            # Вместо простого текста создаем полноценный объект элемента
            item = QListWidgetItem(text)
            # Пример кастомизации: сделаем текст курсивным или добавим подсказку
            item.setToolTip(f"Это элемент: {text}")
            # Добавляем в список
            self.wg_list.addItem(item)
            self.wg_lineedit.clear()

    def remove_selected_items(self) :
        """Безопасное удаление нескольких выбранных элементов."""
        # Получаем список всех выделенных объектов QListWidgetItem
        selected_items = self.wg_list.selectedItems()

        if not selected_items :
            return

        # Удаляем элементы с конца, чтобы индексы не смещались в цикле
        for item in selected_items :
            # Находим индекс (строку) элемента
            row = self.wg_list.row(item)
            # takeItem удаляет элемент из виджета по индексу
            self.wg_list.takeItem(row)

    def sort_items(self) :
        """Сортировка по возрастанию в алфавитном порядке"""
        self.wg_list.sortItems(Qt.SortOrder.AscendingOrder)



# -----------------------------------------------------------------------------

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = ListWidgetAdvancedExample()
    window.show()
    sys.exit(app.exec())