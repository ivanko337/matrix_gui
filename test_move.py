#!/usr/bin/env python3
#coding=utf-8

#from PyQt4 import QtCore, QtGui
from PyQt5 import QtWidgets, QtCore
from numpy import power, sqrt

class DragButton(QtWidgets.QLineEdit):

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def getLen(self, x1, x2, y1, y2):
        return sqrt( power(x1 - x2, 2) + power(y1 - y2, 2) )

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            len = self.getLen(self.pos().x(), 100, self.pos().y(), 100)
            if len < 20:
                currPos = self.mapToGlobal(QtCore.QPoint(100, 100))
            else:
                currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragButton, self).mouseReleaseEvent(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = QtWidgets.QMainWindow()
    w.resize(800,600)

    button = DragButton(w)

    w.show()
    app.exec_()
