# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("MainWindow")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 741, 251))

        self.openFileButton = QtWidgets.QPushButton("Открыть файл", self)
        self.openFileButton.setGeometry(QtCore.QRect(462, 310, 311, 28))
        self.openFileButton.clicked.connect(self.getFileName)

        self.pushButton_2 = QtWidgets.QPushButton("Анализ текста", self)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 490, 311, 28))

        self.openfile = ""

    def getFileName(self):
        dirlist = QFileDialog.getOpenFileName(self)
        self.openfile = dirlist[0]
        print(self.openfile)
        file = open(self.openfile)
        s = ""
        for line in file:
            s += line
        file.close()
        print(s)
        self.textEdit.setText(s)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
