from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt

# создания приложения
app = QApplication([])

# создание и настройка окна
window = QWidget()
window.show()
window.setWindowTitle('Тест')
window.resize(400, 300)

# направляющие:
vertical_line = QVBoxLayout()
horizontal_line = QHBoxLayout()

# виджеты:
text1 = QLabel('Привет')
text2 = QLabel('Пока')
btn = QPushButton('НАЖМИ')

# закрепление виджетов текста на горизонтальной направляющей
horizontal_line.addWidget(text1, alignment=Qt.AlignCenter)
horizontal_line.addWidget(text2, alignment=Qt.AlignCenter)

# закрепление виджета кнопки и гориз. направляющей на вертикальной
vertical_line.addWidget(btn, alignment=Qt.AlignCenter)
vertical_line.addLayout(horizontal_line)

# установка главной напрявляющей для окна
window.setLayout(vertical_line)

# ===========функционал================

# функция смены текста
def switch_text():
    text1.setText('Здарова')

# подключение функции на кнопку
btn.clicked.connect(switch_text)

# запуск приложение
app.exec()