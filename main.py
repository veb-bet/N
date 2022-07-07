# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


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
        
        self.pushButton = QtWidgets.QPushButton("Открыть из файла", self)
        self.pushButton.setGeometry(QtCore.QRect(462, 310, 311, 28))

        self.pushButton_2 = QtWidgets.QPushButton("Анализировать эмоции", self)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 400, 311, 28))

        self.pushButton_3 = QtWidgets.QPushButton("Анализировать психологические расстройства", self)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 490, 311, 28))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
