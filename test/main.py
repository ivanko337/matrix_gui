#!/usr/bin/env python3
#coding=utf-8

import sys
from PyQt5 import QtWidgets, QtCore
import create_matrix
import enter_matrix
import os

class ExampleApp(QtWidgets.QMainWindow, create_matrix.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.checkBox_randomValues.stateChanged.connect(self.randomValuesCheckBoxStateChanged)
		self.checkBox_triangularMatrix_1.stateChanged.connect(self.triangleMatrix1CheckBoxStateChenged)
		self.checkBox_triangularMatrix_2.stateChanged.connect(self.triangleMatrix2CheckBoxStateChenged)
		self.checkBox_unitMatrix.stateChanged.connect(self.unitMatrixCheckBoxStateChenged)
		self.pushButton_create.clicked.connect(self.create)
		#self.entermatrix

	# оказалось неработающим говном, но это ещё не точно
	def dryOneLove(self):
		self.checkBox_randomValues.setChecked(False)
		self.checkBox_triangularMatrix_1.setChecked(False)
		self.checkBox_triangularMatrix_2.setChecked(False)
		self.checkBox_unitMatrix.setChecked(False)

	def randomValuesCheckBoxStateChanged(self, state):
		#self.dryOneLove()
		#self.checkBox_randomValues.setChecked(True)
		if state == QtCore.Qt.Checked:
			self.checkBox_triangularMatrix_1.setChecked(False)
			self.checkBox_triangularMatrix_2.setChecked(False)
			self.checkBox_unitMatrix.setChecked(False)

	def unitMatrixCheckBoxStateChenged(self, state):
		#self.dryOneLove()
		#self.checkBox_unitMatrix.setChecked(True)
		if state == QtCore.Qt.Checked:
			self.checkBox_randomValues.setChecked(False)
			self.checkBox_triangularMatrix_1.setChecked(False)
			self.checkBox_triangularMatrix_2.setChecked(False)

	def triangleMatrix1CheckBoxStateChenged(self, state):
		if state == QtCore.Qt.Checked:
			self.checkBox_randomValues.setChecked(False)
			self.checkBox_unitMatrix.setChecked(False)
			self.checkBox_triangularMatrix_2.setChecked(False)

	def triangleMatrix2CheckBoxStateChenged(self, state):
		if state == QtCore.Qt.Checked:
			self.checkBox_randomValues.setChecked(False)
			self.checkBox_unitMatrix.setChecked(False)
			self.checkBox_triangularMatrix_1.setChecked(False)

	def create(self):
		print('create matrix {} x {}'.format(self.lineEdit_rows.text(), self.lineEdit_columns.text()))
		enter_matrix.__main__()

def __main__():
	app = QtWidgets.QApplication(sys.argv) # Новый экземпляр QApplication
	window = ExampleApp()  # Создаём объект класса ExampleApp
	window.show()  # Показываем окно
	window.setFixedSize(window.width(), window.height())
	app.exec_()  # и запускаем приложение

if __name__ == '__main__':
	__main__()
