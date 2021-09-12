from PyQt5 import QtWidgets
import fin_wind
import MAI

class FIN(QtWidgets.QMainWindow, fin_wind.Ui_MainWindow):
    def __init__(self, rez, mass_alter):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setGeometry(300, 300, 1024, 512)
        itog = ''
        best = ''
        max = 0
        for i in range(len(rez)):
            itog += mass_alter[i] + '\t' + str(rez[i])[1:-1] + '\n'
            if float(str(rez[i])[1:-1]) > max:
                max = float(str(rez[i])[1:-1])
                best = mass_alter[i]

        self.textBrowser.setText(itog)
        self.lineEdit.setText(best)
        self.btn_close.clicked.connect(self.close)
        self.btn_new.clicked.connect(self.restart)
        print(rez)

    def restart(self):
        global wind3
        wind3 = MAI.Start()  # Создаём объект класса ExampleApp
        wind3.show()  # Показываем окно
        self.close()