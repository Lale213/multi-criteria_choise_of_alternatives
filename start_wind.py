# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start_wind.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 140)
        MainWindow.setMinimumSize(QtCore.QSize(550, 140))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Alternat = QtWidgets.QLineEdit(self.centralwidget)
        self.Alternat.setObjectName("Alternat")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Alternat)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Kriter = QtWidgets.QLineEdit(self.centralwidget)
        self.Kriter.setObjectName("Kriter")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Kriter)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????? ??????????????????????"))
        self.label.setText(_translate("MainWindow", "?????????????? ???????????????????? ??????????????????:"))
        self.label_2.setText(_translate("MainWindow", "?????????????? ???????????????????? ??????????????????????:"))
        self.checkBox.setText(_translate("MainWindow", "???????????????????????? ???????????????? ???? ??????????????????"))
        self.pushButton.setText(_translate("MainWindow", "???????????????????? ?? ??????????????"))
