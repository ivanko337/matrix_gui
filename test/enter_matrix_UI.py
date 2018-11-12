# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_matrix.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(187, 125)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_2.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_2.addWidget(self.lineEdit_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_2.addWidget(self.lineEdit_13)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.horizontalLayout_3.addWidget(self.lineEdit_21)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.horizontalLayout_3.addWidget(self.lineEdit_22)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.horizontalLayout_3.addWidget(self.lineEdit_23)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.horizontalLayout.addWidget(self.lineEdit_31)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.horizontalLayout.addWidget(self.lineEdit_32)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.horizontalLayout.addWidget(self.lineEdit_33)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.lineEdit_11.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enter Matrix"))