# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("SSIMP")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 741, 251))

        self.openFileButton = QtWidgets.QPushButton("Open file", self)
        self.openFileButton.setGeometry(QtCore.QRect(460, 310, 311, 28))

        self.pushButton_1 = QtWidgets.QPushButton("Clear", self)
        self.pushButton_1.setGeometry(QtCore.QRect(460, 400, 311, 28))

        self.pushButton_2 = QtWidgets.QPushButton("Text analysis", self)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 490, 311, 28))

        self.label_1 = QtWidgets.QLabel("Statistics of psychological disorders:", self)
        self.label_1.setGeometry(QtCore.QRect(30, 530, 400, 28))
        
        self.label_2 = QtWidgets.QLabel("Statistics on the absence of psychological disorders:", self)
        self.label_2.setGeometry(QtCore.QRect(30, 550, 400, 28))

        #------------------------
        self.frame = QtWidgets.QFrame(self)
        self.frame.setStyleSheet("background-color: lightBlue;")
        self.frame.setGeometry(QtCore.QRect(30, 290, 350, 230))

        self.layount = QVBoxLayout(self.frame)
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.layount.addWidget(self.canvas)
        #------------------------
        
        self.openFileButton.clicked.connect(self.getFileName)
        self.pushButton_1.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.dostoevsky)
        
        self.openfile = ""
        self.s = ""

        self.psix = 0
        self.nepsix = 0
        

    def getFileName(self):
        dirlist = QFileDialog.getOpenFileName(self)
        self.openfile = dirlist[0]
        print(self.openfile)

        try:
            if self.openfile != "" and "." in self.openfile:
                file = open(self.openfile)
                self.s = ""
                for line in file:
                    self.s += line.lower()
                file.close()
                self.textEdit.setText(self.s)
        except:
            try:
                if self.openfile != "" and "." in self.openfile:
                    file = open(self.openfile, encoding="utf-8")
                    self.s = ""
                    for line in file:
                        self.s += line.lower()
                    file.close()
                    self.textEdit.setText(self.s)
            except:
                self.textEdit.setText("File reading error")
                
        self.figure.clear()
        self.canvas.draw()

    def clear(self):
        self.textEdit.setText("")

        self.psix = 0
        self.nepsix = 0
        self.label_1.setText("Statistics of psychological disorders:")
        self.label_2.setText("Statistics on the absence of psychological disorders:")

        self.figure.clear()
        self.canvas.draw()


    def dostoevsky(self):
        from dostoevsky.tokenization import RegexTokenizer
        from dostoevsky.models import FastTextSocialNetworkModel
        tokenizer = RegexTokenizer()
        model = FastTextSocialNetworkModel(tokenizer=tokenizer)

        ban_words = []
        try:
            file = open("2.txt", encoding="utf-8")
            for line in file:
                s = line.strip()
                ban_words.append(s)
            file.close()
        except:
            None
        self.s = self.textEdit.toPlainText()
        
        messages = list(self.s.split("\n"))
        messages = [x.lower() for x in messages if len(x) > 5]

            #if not("Yes" in messages[i] or "No" in messages[i]):
                       
        results = model.predict(messages, k=5)

        self.s = ""

        self.psix = 0
        self.nepsix = 0

        for message, sentiment in zip(messages, results):
            positive = round(sentiment["positive"], 5)
            negative = round(sentiment["negative"], 5)
            neutral = round(sentiment["neutral"], 5)
            speech = round(sentiment["speech"], 5)
            skip = round(sentiment["skip"], 5)
            m = max(positive, negative, neutral, speech, skip)
            self.s += message
            k = False
            for i in ban_words:
                if i in message:
                    k = True
                    break
            
            if m == negative or negative > 0.5 or k:
                if not("there are symptoms of psychological disorders" in message or "there are no psychological disorders" in message):
                    self.s += "   ->    There are symptoms of psychological disorders\n"
                    self.psix += 1
                else:
                    if "there are symptoms of psychological disorders" in message:
                        self.psix += 1
                    else:
                        self.nepsix += 1
                    self.s += "\n"
                
            else:
                if not("there are symptoms of psychological disorders" in message or "there are no psychological disorders" in message):
                    self.s += "   ->    There are no psychological disorders\n"
                    self.nepsix += 1
                else:
                    if "there are symptoms of psychological disorders" in message:
                        self.psix += 1
                    else:
                        self.nepsix += 1
                    self.s += "\n"
                    
        self.textEdit.setText(self.s)
        self.label_1.setText(f"Statistics of psychological disorders:   {self.psix}/{self.psix + self.nepsix}")
        self.label_2.setText(f"Statistics on the absence of psychological disorders:   {self.nepsix}/{self.psix + self.nepsix}")

        #----------Diagramma-----------
        if self.psix + self.nepsix != 0:
            data = [self.psix, self.nepsix]
            disorders = ["SPD", "SAPD"]
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            #fig, ax = plt.subplots()
            ax.pie(data, labels=disorders, wedgeprops=dict(width=0.5))
            leg = ax.legend(loc='center', bbox_to_anchor=(0, -0.07), shadow=False, ncol=2)

            self.canvas.draw()
            
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
