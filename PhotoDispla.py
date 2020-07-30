# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PhotoDispla.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhotoDisplay(object):
    def setupUi(self, PhotoDisplay):
        PhotoDisplay.setObjectName("PhotoDisplay")
        PhotoDisplay.resize(560, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PhotoDisplay.sizePolicy().hasHeightForWidth())
        PhotoDisplay.setSizePolicy(sizePolicy)
        PhotoDisplay.setMinimumSize(QtCore.QSize(560, 560))
        PhotoDisplay.setMaximumSize(QtCore.QSize(560, 560))
        self.centralwidget = QtWidgets.QWidget(PhotoDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 560, 60))
        self.frame.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 15, 90, 30))
        self.pushButton.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 15, 90, 30))
        self.pushButton_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(240, 15, 60, 30))
        self.label.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 220, 20))
        self.label_2.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(0, 60, 560, 500))
        self.Image.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.Image.setText("")
        self.Image.setObjectName("Image")
        PhotoDisplay.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhotoDisplay)
        QtCore.QMetaObject.connectSlotsByName(PhotoDisplay)

    def retranslateUi(self, PhotoDisplay):
        _translate = QtCore.QCoreApplication.translate
        PhotoDisplay.setWindowTitle(_translate("PhotoDisplay", "MainWindow"))
        self.pushButton.setText(_translate("PhotoDisplay", "Previous"))
        self.pushButton_2.setText(_translate("PhotoDisplay", "Next"))

