# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_matrix.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_randomValues = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_randomValues.setChecked(False)
        self.checkBox_randomValues.setObjectName("checkBox_randomValues")
        self.verticalLayout.addWidget(self.checkBox_randomValues)
        self.checkBox_unitMatrix = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_unitMatrix.setObjectName("checkBox_unitMatrix")
        self.verticalLayout.addWidget(self.checkBox_unitMatrix)
        self.checkBox_triangularMatrix_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_triangularMatrix_1.setObjectName("checkBox_triangularMatrix_1")
        self.verticalLayout.addWidget(self.checkBox_triangularMatrix_1)
        self.checkBox_triangularMatrix_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_triangularMatrix_2.setObjectName("checkBox_triangularMatrix_2")
        self.verticalLayout.addWidget(self.checkBox_triangularMatrix_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_rows = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_rows.setObjectName("lineEdit_rows")
        self.horizontalLayout.addWidget(self.lineEdit_rows)
        self.lineEdit_columns = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_columns.setObjectName("lineEdit_columns")
        self.horizontalLayout.addWidget(self.lineEdit_columns)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setObjectName("pushButton_create")
        self.verticalLayout_2.addWidget(self.pushButton_create)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Параметры матрицы"))
        self.checkBox_randomValues.setText(_translate("MainWindow", "Заполнить случайными значениями"))
        self.checkBox_unitMatrix.setText(_translate("MainWindow", "Еденичная матрица"))
        self.checkBox_triangularMatrix_1.setText(_translate("MainWindow", "Треугольная матрица 1"))
        self.checkBox_triangularMatrix_2.setText(_translate("MainWindow", "Треугольная матрица 2"))
        self.label.setText(_translate("MainWindow", "Кол-во строк"))
        self.label_2.setText(_translate("MainWindow", "Кол-во столбцов"))
        self.lineEdit_rows.setText(_translate("MainWindow", "0"))
        self.lineEdit_columns.setText(_translate("MainWindow", "0"))
        self.pushButton_create.setText(_translate("MainWindow", "Создать матрицу"))

