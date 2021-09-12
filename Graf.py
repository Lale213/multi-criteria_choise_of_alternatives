from PyQt5 import QtWidgets
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import Graf_wind
import Error
import para


class Graf_ierar(QtWidgets.QMainWindow, Graf_wind.Ui_MainWindow):
    def __init__(self, next, flag):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        X = max(next[0], next[1])
        self.setGeometry(0, 0, X * 155, 300)
        self.tableKrit.setRowCount(1)
        self.tableKrit.setColumnCount(next[1])
        self.tableAlter.setRowCount(1)
        self.tableAlter.setColumnCount(next[0])
        self.pushButton.clicked.connect(lambda: self.get_data(flag))  # Выполнить функцию при нажатии кнопки
        if flag == 1:
            self.lineTarget.setText('Наилучшая СОВ')
            mass_alter = ['Snort',
                          'Check Point Endpoint Security',
                          'Prelude Hybrid IDS',
                          'IBM Security Network Intrusion Prevention System',
                          'Untangle',
                          'MCAfee']
            mass_kriter = ['Самозащита', 'Используемый метод обнаружения вторжения',
                          'Возможность и актуальность обновления  баз данных сигнатур',
                          'Адекватная реакция на обнаруженную атаку',
                          'Расширяемость', 'Архитектура СОКА',
                          'Требуемые ресурсы компьютерной системы',
                          'Стоимость', 'Адаптация системы к незнакомым атакам']
            for i in range(self.tableKrit.columnCount()):
                item = QtWidgets.QTableWidgetItem(mass_kriter[i])
                self.tableKrit.setItem(0, i, item)
            for i in range(self.tableAlter.columnCount()):
                item = QtWidgets.QTableWidgetItem(mass_alter[i])
                self.tableAlter.setItem(0, i, item)

    def get_data(self, flag):
        mass_alter = []
        mass_kriter = []
        try:
            for i in range(self.tableKrit.columnCount()):
                if self.tableKrit.item(0, i).text() == '':
                    Error.ERROR(2)
                    return 0
                mass_kriter.append(self.tableKrit.item(0, i).text())
            for i in range(self.tableAlter.columnCount()):
                if self.tableAlter.item(0, i).text() == '':
                    Error.ERROR(2)
                    return 0
                mass_alter.append(self.tableAlter.item(0, i).text())
        except:
            Error.ERROR(2)
            return 0
        if self.lineTarget.text() == '':
            Error.ERROR(3)

        else:
            global wind1
            DATA = []
            wind1 = para.Poparno(mass_kriter, mass_alter, -1, flag, DATA)
            wind1.show()
            self.close()
