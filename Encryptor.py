# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Encryptor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(480, 240)
        Login.setMinimumSize(QtCore.QSize(480, 240))
        Login.setMaximumSize(QtCore.QSize(480, 240))
        Login.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(25, 50, 430, 40))
        self.lineEdit.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(25, 150, 93, 30))
        self.pushButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(365, 150, 90, 30))
        self.pushButton_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton_2.setObjectName("pushButton_2")
        Login.setCentralWidget(self.centralwidget)
        self.actionEncrypt = QtWidgets.QAction(Login)
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.actionDecrypt = QtWidgets.QAction(Login)
        self.actionDecrypt.setObjectName("actionDecrypt")
        self.actionBackup = QtWidgets.QAction(Login)
        self.actionBackup.setObjectName("actionBackup")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.pushButton.setText(_translate("Login", "Akcepti"))
        self.pushButton_2.setText(_translate("Login", "Nuligi"))
        self.actionEncrypt.setText(_translate("Login", "Encrypt"))
        self.actionDecrypt.setText(_translate("Login", "Decrypt"))
        self.actionBackup.setText(_translate("Login", "Backup"))

