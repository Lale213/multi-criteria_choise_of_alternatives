from PyQt5 import QtWidgets
import Error_wind


def ERROR(code):
    global window
    if code == 1:
        window = Error_1()  # неверные значения
    elif code == 2:
        window = Error_2()
    elif code == 3:
        window = Error_3()
    elif code == 4:
        window = Error_4()
    elif code == 5:
        window = Error_5()
    window.show()  # Показываем окно



class Error_1(QtWidgets.QMainWindow, Error_wind.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.label.setText('Ошибка!\n\nВведите целые числа от 1 до 9.')


class Error_2(QtWidgets.QMainWindow, Error_wind.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.label.setText('Ошибка!\n\nЗаполните таблицу.')


class Error_3(QtWidgets.QMainWindow, Error_wind.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.label.setText('Ошибка!\n\nВведите цель выбора!')

class Error_4(QtWidgets.QMainWindow, Error_wind.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.label.setText('Ошибка!\n\nМатрица не согласована!')

class Error_5(QtWidgets.QMainWindow, Error_wind.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.label.setText('Ошибка!\n\nМатрица заполнена неверно!')
