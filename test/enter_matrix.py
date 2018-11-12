#coding=utf-8

import sys
from PyQt5 import QtWidgets, QtCore
import enter_matrix_UI
import os

class EnterMatrix(QtWidgets.QMainWindow, enter_matrix_UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)