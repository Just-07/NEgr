import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Установка цвета фона
        self.setStyleSheet("background-color: lightgreen;")
        self.setWindowTitle('MOG')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()

    # Создание вертикального контейнера для размещения кнопок
    vertical_layout = QVBoxLayout(ex)

    # Создание кнопок
    down1 = QPushButton("СКАЧАТЬ    ПЕСНЮ")
    remix1 = QPushButton("ИЗМЕНИТЬ  СКОРОСТЬ")
    remix2 = QPushButton("ИЗМЕНИТЬ  БИТ")
    remix3 = QPushButton("ИЗМЕНИТЬ  ЗВУК")
    remix4 = QPushButton("ДОБАВИТЬ  ЭФФЕКТЫ")
    time1 = QPushButton("УБРАТЬ     ПРОМЕЖУТОК")
    time2 = QPushButton("ДОБАВИТЬ   ПРОМЕЖУТОК")


    down1.setStyleSheet("background-color: blue")
    remix1.setStyleSheet("background-color: blue")
    remix2.setStyleSheet("background-color: blue")
    remix3.setStyleSheet("background-color: blue")
    remix4.setStyleSheet("background-color: blue")
    time1.setStyleSheet("background-color: blue")
    time2.setStyleSheet("background-color: blue")

    # Добавление кнопок в вертикальный контейнер
    vertical_layout.addWidget(down1)
    vertical_layout.addWidget(remix1)
    vertical_layout.addWidget(remix2)
    vertical_layout.addWidget(remix3)
    vertical_layout.addWidget(remix4)
    vertical_layout.addWidget(time1)
    vertical_layout.addWidget(time2)

    ex.show()
    sys.exit(app.exec_())