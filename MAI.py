from PyQt5 import QtWidgets
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import start_wind
import Error
import Graf


class Start(QtWidgets.QMainWindow, start_wind.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.Enter)  # Выполнить функцию при нажатии кнопки
        self.checkBox.stateChanged.connect(lambda x: self.change() if x else self.disable_slot())


    def Enter(self):
        try:
            alternativ = int(self.Alternat.text())
            krit = int(self.Kriter.text())
            if alternativ < 1 or krit < 1 or alternativ > 9 or krit > 9:
                Error.ERROR(1)
            else:
                if self.checkBox.isChecked():
                    flag = 1
                else:
                    flag = 0
                next = [krit, alternativ]
                global window
                window = Graf.Graf_ierar(next, flag)
                window.show()
                self.close()
        except ValueError:
            Error.ERROR(1)

    def change(self):
        self.Alternat.setText('9')
        self.Kriter.setText('6')
        self.Alternat.setEnabled(False)
        self.Kriter.setEnabled(False)

    def disable_slot(self):
        self.Alternat.setText('')
        self.Kriter.setText('')
        self.Alternat.setEnabled(True)
        self.Kriter.setEnabled(True)