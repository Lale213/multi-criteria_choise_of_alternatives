from PyQt5 import QtWidgets, QtCore
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import Error
import numpy as np
import math
import popara_wind
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import fin
import matplotlib.dates as mdates
import datetime as dt
import csv

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter

class Poparno(QtWidgets.QMainWindow, popara_wind.Ui_MainWindow):
    def __init__(self, mass_kriter, mass_alter, i, flag, DATA):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        # self.tableWidget.setHorizontalHeaderLabels(mass_alter)
        # self.tableWidget.setVerticalHeaderLabels(mass_alter)
        if i == -1:
            self.label.setText('')
            mass_alter, mass_kriter = mass_kriter, mass_alter
            DATA = []
        else:
            self.label.setText(mass_kriter[i])
        LEN = len(mass_alter)
        if LEN < 10:
            self.setGeometry(0, 0, LEN * 150 + 300, LEN * 70 + 60)
        else:
            self.setGeometry(0, 0, 9 * 180 + 300, 9 * 100 + 300)

        self.btn_next.clicked.connect(
            lambda: self.dalee(mass_kriter, mass_alter, i, flag, DATA))  # Выполнить функцию при нажатии кнопки
        self.btn_graf.setEnabled(False)
        self.btn_next.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.tableWidget.setRowCount(LEN)
        self.tableWidget.setColumnCount(LEN)
        self.btn_graf.clicked.connect(lambda: self.make_graf_pie(mass_alter))
        self.pushButton.clicked.connect(lambda: self.make_graf_stolb(mass_alter))
        delegate = AlignDelegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)
        stylesheet = "::section{Background-color:rgb(176,196,222)}"
        self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        self.tableWidget.verticalHeader().setStyleSheet(stylesheet)
        if i == -1:
            TEXT = 'Критерии: \n'
            self.label.setText('Попарная оценка критериев')
            if flag == 1:
                data = self.check_data(-1)
                for j in range(LEN):
                    for q in range(LEN):
                        item = QtWidgets.QTableWidgetItem(data[j][q])
                        self.tableWidget.setItem(j, q, item)

            else:
                data = np.eye(LEN)
                for j in range(LEN):
                    for q in range(LEN):
                        item = QtWidgets.QTableWidgetItem(str(int(data[j][q])))
                        self.tableWidget.setItem(j, q, item)

        else:
            TEXT = 'Альтернативы: \n'
        for q in range(len(mass_alter)):
            TEXT += str(q + 1) + ': ' + mass_alter[q] + '\n'
        self.textEdit.setText(TEXT)
        if flag == 0:
            data = np.eye(LEN)
            for j in range(LEN):
                for q in range(LEN):
                    item = QtWidgets.QTableWidgetItem(str(int(data[j][q])))
                    self.tableWidget.setItem(j, q, item)
        else:
            data = self.check_data(i)
            for j in range(LEN):
                for q in range(LEN):
                    item = QtWidgets.QTableWidgetItem(data[j][q])
                    self.tableWidget.setItem(j, q, item)
        self.btn_chek.clicked.connect(lambda: self.CHEK(LEN))

    def dalee(self, mass_kriter, mass_alter, i, flag, DATA):
        # print(len(mass_alter))
        data = self.lineEdit.text().split(' ')[4:4 + len(mass_alter)]
        # print(data)
        new_data = []
        for r in data:
            r = r[:-1]
            new_data.append(float(r))
        data = dict(zip(mass_alter, new_data))
        DATA.append(new_data)
        if i == -1:
            sorted_dict = {}
            sorted_keys = sorted(data, key=data.get)
            for w in sorted_keys:
                sorted_dict[w] = data[w]
            # print(sorted_dict)
            temp_mass = []
            for j in sorted_dict.keys():
                temp_mass.append(j)
            mass_alter = temp_mass
            # print(mass_alter)
            mass_alter, mass_kriter = mass_kriter, mass_alter
        global wind
        i += 1
        if i < len(mass_kriter):
            wind = Poparno(mass_kriter, mass_alter, i, flag, DATA)
            wind.show()
            self.close()
        else:
            alter = []
            krit = DATA[0]
            krit.sort()
            krit = np.array(krit)
            for k in range(1, len(DATA)):
                alter.append(DATA[k])
            alter = np.array(alter).T
            rez = alter.dot(krit[np.newaxis, :].T)
            print(rez)
            print(mass_alter)
            global wind2
            wind2 = fin.FIN(rez, mass_alter)
            wind2.show()
            self.close()

    def CHEK(self, LEN):
        data = []
        try:
            for j in range(LEN):
                data1 = []
                for q in range(LEN):
                    if self.tableWidget.item(j, q).text() == '':
                        Error.ERROR(5)
                        return 0
                    if '/' in self.tableWidget.item(j, q).text():
                        temp2 = self.tableWidget.item(j, q).text().split('/')
                        temp = int(temp2[0]) / int(temp2[1])

                    else:
                        temp = int(self.tableWidget.item(j, q).text())
                    if int(temp) == 0:
                        temp = 1 / int(self.tableWidget.item(q, j).text())
                        item = QtWidgets.QTableWidgetItem('1/' + self.tableWidget.item(q, j).text())
                        self.tableWidget.setItem(j, q, item)
                    try:
                        if int(self.tableWidget.item(j, q).text()) < 0:
                            Error.ERROR(5)
                            return 0
                    except:
                        pass
                    data1.append(temp)
                data.append(data1)
            delegate = AlignDelegate(self.tableWidget)
            self.tableWidget.setItemDelegate(delegate)
        except:
            Error.ERROR(5)
            return 0
        vector_prior, flag2, OS, IS = self.magic(data)
        if not flag2:
            Error.ERROR(4)
            self.lineEdit.setText('; ИС = ' + str(IS) + '; ОС = ' + str(OS) + ' < 0.1 => Матрица НЕ согласована!')

        else:
            text = "Значения весов удельных критериев: "
            for i in vector_prior:
                text += str(i) + ', '
            text = text.strip(', ')

            text += '; ИС = ' + str(IS) + '; ОС = ' + str(OS) + ' < 0.1 => Матрица согласована!'
            self.lineEdit.setText(text)
            self.btn_next.setEnabled(True)
            self.btn_graf.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.btn_chek.setEnabled(False)

    def magic(self, data):
        vector_prior = []
        for i in data:
            pop = 1
            for j in i:
                pop *= j
            pop = math.pow(pop, 1 / len(i))
            vector_prior.append(pop)
        # print(vector_prior)
        # print(sum(vector_prior))
        vector_prior2 = []
        for i in range(len(vector_prior)):
            vector_prior2.append(vector_prior[i] / sum(vector_prior))
        vector_prior = vector_prior2
        data = np.array(data)
        vector_prior = np.array(vector_prior)
        vector_prior2 = data.dot(vector_prior)
        # print(vector_prior2)
        vector_prior2 /= vector_prior
        # print(vector_prior2)
        l_max = sum(vector_prior2) / len(vector_prior2)
        # print(l_max)
        IS = (l_max - len(vector_prior2)) / (len(vector_prior2) - 1)
        # print('IS = ' + str(IS))
        midSI = self.check_SI(len(vector_prior2))
        OS = IS / midSI
        # print('OS = ' + str(OS))
        if str(OS) == 'nan':
            OS = 0
        if OS < 0.1:
            return vector_prior, True, OS, IS
        else:
            return vector_prior, False, OS, IS

    def check_SI(self, n):
        Sl_soglas = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.40, 9: 1.45, 10: 1.49, 11: 1.5,
                     12: 1.48, 13: 1.56, 14: 1.57, 15: 1.59}
        return Sl_soglas[n]

    def make_graf_pie(self, mass_alter):
        data = self.lineEdit.text().split(' ')[4:4 + len(mass_alter)]
        upd_data = []
        for i in data:
            i = i[:-1]
            upd_data.append(float(i))

        dpi = 80
        fig = plt.figure(dpi=dpi, figsize=(1536 / dpi, 768 / dpi))
        mpl.rcParams.update({'font.size': 13})

        plt.title('Удельные веса.')

        xs = range(len(mass_alter))
        plt.pie(
            upd_data, radius=1.1, autopct='%.1f')
        plt.legend(
            bbox_to_anchor=(0.15, 0.25), labels=mass_alter)
        fig.show()

    def make_graf_stolb(self, mass_alter):
        data = self.lineEdit.text().split(' ')[4:4 + len(mass_alter)]
        upd_data = []
        for i in data:
            i = i[:-1]
            upd_data.append(float(i))

        frequencies = upd_data
        freq_series = pd.Series(frequencies)
        y_labels = range(1, len(mass_alter) + 1)
        # Plot the figure.
        plt.figure(figsize=(12, 8))
        ax = freq_series.plot(kind='barh')
        ax.set_title('Удельные веса')
        ax.set_xlim(0, max(upd_data) + 0.2)  # expand xlim to make labels easier to read
        ax.set_yticklabels(y_labels)

        rects = ax.patches

        # For each bar: Place a label
        for h, rect in enumerate(rects):
            # Get X and Y placement of label from rect.
            x_value = rect.get_width()
            y_value = rect.get_y() + rect.get_height() / 2

            # Number of points between bar and label. Change to your liking.
            space = 5
            # Vertical alignment for positive values
            ha = 'left'

            # If value of bar is negative: Place label left of bar
            if x_value < 0:
                # Invert space to place label to the left
                space *= -1
                # Horizontally align label at right
                ha = 'right'

            # Use X value as label and format number with one decimal place
            label = "{}".format(mass_alter[h])
            # Create annotation
            plt.annotate(
                label,  # Use `label` as label
                (x_value, y_value),  # Place label at end of the bar
                xytext=(space, 0),  # Horizontally shift label by `space`
                textcoords="offset points",  # Interpret `xytext` as offset in points
                va='center',  # Vertically center label
                ha=ha)  # Horizontally align label differently for
            # positive and negative values.
        plt.show()

    def check_data(self, i):
        if i == -1:
            data = np.array([['1', '0', '3', '0', '5', '5', '5', '7', '1'],
                             ['3', '1', '9', '1', '9', '9', '8', '9', '3'],
                             ['0', '0', '1', '0', '1', '2', '1', '2', '0'],
                             ['3', '1', '7', '1', '7', '9', '9', '8', '3'],
                             ['0', '0', '1', '0', '1', '1', '1', '2', '0'],
                             ['0', '0', '0', '0', '1', '1', '1', '2', '0'],
                             ['0', '0', '1', '0', '1', '1', '1', '2', '0'],
                             ['0', '0', '0', '0', '0', '0', '0', '1', '0'],
                             ['1', '0', '3', '0', '3', '5', '5', '7', '1']])
        elif i == 0:
            data = np.array([['1', '3', '1', '9', '3', '5'],
                             ['0', '1', '0', '6', '1', '3'],
                             ['1', '3', '1', '9', '3', '5'],
                             ['0', '0', '0', '1', '0', '0'],
                             ['0', '1', '0', '5', '1', '2'],
                             ['0', '0', '0', '3', '0', '1']])
        elif i == 1:
            data = np.array([['1', '0', '0', '0', '0', '0'],
                             ['5', '1', '1', '1', '1', '1'],
                             ['5', '1', '1', '1', '1', '1'],
                             ['5', '1', '1', '1', '1', '1'],
                             ['5', '1', '1', '1', '1', '1'],
                             ['5', '1', '1', '1', '1', '1']])
        elif i == 2:
            data = np.array([['1', '0', '3', '5', '7', '1'],
                             ['3', '1', '7', '8', '9', '3'],
                             ['0', '0', '1', '2', '5', '0'],
                             ['0', '0', '0', '1', '1', '0'],
                             ['0', '0', '0', '1', '1', '0'],
                             ['1', '0', '2', '5', '7', '1']])
        elif i == 3:
            data = np.array([['1', '7', '0', '3', '2', '3'],
                             ['0', '1', '0', '0', '0', '0'],
                             ['3', '9', '1', '7', '3', '9'],
                             ['0', '3', '0', '1', '0', '1'],
                             ['0', '4', '0', '2', '1', '2'],
                             ['0', '2', '0', '1', '0', '1']])
        elif i == 4:
            data = np.array([['1', '0', '0', '0', '2', '0'],
                             ['2', '1', '0', '0', '3', '0'],
                             ['3', '2', '1', '0', '5', '0'],
                             ['7', '3', '5', '1', '9', '3'],
                             ['0', '0', '0', '0', '1', '0'],
                             ['6', '5', '2', '0', '7', '1']])
        elif i == 5:
            data = np.array([['1', '0', '0', '0', '1', '0'],
                             ['2', '1', '1', '0', '3', '0'],
                             ['2', '1', '1', '0', '2', '0'],
                             ['4', '2', '2', '1', '5', '1'],
                             ['1', '0', '0', '0', '1', '0'],
                             ['4', '2', '3', '1', '5', '1']])
        elif i == 6:
            data = np.array([['1', '0', '0', '0', '0', '0'],
                             ['2', '1', '0', '0', '0', '1'],
                             ['4', '2', '1', '0', '2', '2'],
                             ['5', '3', '2', '1', '2', '3'],
                             ['3', '2', '0', '0', '1', '1'],
                             ['2', '1', '0', '0', '1', '1']])
        elif i == 7:
            data = np.array([['1', '0', '0', '0', '1', '0'],
                             ['3', '1', '2', '0', '3', '0'],
                             ['2', '0', '1', '0', '2', '0'],
                             ['7', '3', '3', '1', '6', '2'],
                             ['1', '0', '0', '0', '1', '0'],
                             ['2', '2', '3', '0', '4', '1']])
        elif i == 8:
            data = np.array([['1', '0', '0', '0', '0', '0'],
                             ['2', '1', '2', '0', '0', '0'],
                             ['2', '0', '1', '0', '0', '0'],
                             ['4', '5', '5', '1', '3', '3'],
                             ['3', '3', '3', '0', '1', '1'],
                             ['3', '2', '4', '0', '1', '1']])
        else:
            data = np.eye(9)
        return data
