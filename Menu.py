# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(480, 240)
        Menu.setMinimumSize(QtCore.QSize(480, 240))
        Menu.setMaximumSize(QtCore.QSize(480, 240))
        Menu.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(35, 40, 410, 40))
        self.lineEdit.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(35, 190, 90, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(35, 90, 21, 20))
        self.checkBox.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(355, 190, 90, 30))
        self.pushButton_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(195, 190, 90, 30))
        self.pushButton_3.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(418, 90, 27, 20))
        self.toolButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.toolButton.setObjectName("toolButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(195, 120, 90, 50))
        self.lineEdit_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "MainWindow"))
        self.pushButton.setText(_translate("Menu", "Encrypt"))
        self.pushButton_2.setText(_translate("Menu", "Decrypt"))
        self.pushButton_3.setText(_translate("Menu", "Display"))
        self.toolButton.setText(_translate("Menu", "..."))

