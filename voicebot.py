# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import warnings
warnings.filterwarnings("ignore")

from PyQt5 import QtCore, QtGui, QtWidgets
from model import*
global res
global text

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 617)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("border : 1px solid black;\n"
"background: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #8688ff, \n"
"                          stop: 1 #ffffff );\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 150, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(170, 182, 255);\n"
"\n"
"border-radius : 100;\n"
"border : 2px solid black;}\n"
"QPushButton#pushButton::pressed{\n"
"background-color:black;}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("clipart1184192.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(96, 116))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.call)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 711, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("\n"
"background-color: rgb(170, 182, 255);")
        self.label_2.setLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(260, 160, 452, 153))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(170, 182, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(40, 360, 691, 151))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(170, 182, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(170, 182, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_tulip = QtWidgets.QTextEdit(self.widget1)
        self.textEdit_tulip.setStyleSheet("background-color: rgb(170, 182, 255);")
        self.textEdit_tulip.setObjectName("textEdit_tulip")
        self.verticalLayout_4.addWidget(self.textEdit_tulip)
        self.textEdit_you = QtWidgets.QTextEdit(self.widget1)
        self.textEdit_you.setStyleSheet("background-color: rgb(170, 182, 255);")
        self.textEdit_you.setObjectName("textEdit_you")
        self.textEdit_tulip.setFont(font)
        self.textEdit_you.setFont(font)
       
        self.verticalLayout_4.addWidget(self.textEdit_you)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.pushButton.raise_()
        self.label.raise_()
        self.textEdit_tulip.raise_()
        self.label_2.raise_()
        self.textEdit_tulip.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def print1(self):
        global text
        global res
        self.textEdit_you.setPlainText(res)
        self.textEdit_tulip.setPlainText(text)
        
        self.pushButton.setEnabled(True)
 




    def call(self):
        self.pushButton.setEnabled(False)
        global text
        global res
        global nlp
        global city 
        #global city
        global ex
        ex=True
        recognizer = sr.Recognizer()
        while ex==True:
                with sr.Microphone() as mic:
                        print("listening...")
                        audio = recognizer.listen(mic)
                try:
                        text = recognizer.recognize_google(audio,language="en-US")
                        print("me --> ", text)


                except:
                        text="error"
                        res="I am not getting you"
                
        
                print(text)
                #self.print1(text)

                if wake_up(text) is True:
                        res = "Hello I am Tulip the AI, what can I do for you?"
                
                elif "time" in text:
                        res = action_time()
                        self.textEdit_tulip.setPlainText(res)

                elif "temperature" in text:
                        #global text
                        doc=nlp(text)
                        try:
                                for ent in doc.ents:
                                        if ent.label_=="GPE":
                                                city=ent.text
                        except:
                                city="Delhi"
                        res=action_temp(city)

                elif "weekday" in text:
                        res=action_day()

                elif "date" in text:
                        res=action_date()
                
                elif "weather" in text:
                        doc=nlp(text)
                        try:
                                for ent in doc.ents:
                                        if ent.label_=="GPE":
                                                city=ent.text
                        except:
                                city = "Delhi"
                        res=action_weather(city)


                elif any(i in text for i in ["exit","close"]):
                        res = np.random.choice(["Tata","Have a good day","Bye","Goodbye","Hope to meet soon","peace out!"])
                        #ex=False
                        

                        
                elif any(i in text for i in ["thank","thanks"]):
                        res = np.random.choice(["you're welcome!","anytime!","no problem!","cool!","I'm here if you need me!","peace out!"])

                elif "bye" in text:
                        res=np.random.choice(["Take Care!","Come Back Soon","Bye nice to talk to you"])

                elif "search" in text:
                
                        try:
                                words=text.split()
                                word=words[-1]
                                res=wikisearch(word)
                        except:
                                res="Am Sorry I Don't Know about this"
                text_to_speech(res)
                ex=False
                self.print1()
                



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Press to\n"
"START"))
        self.label_2.setText(_translate("MainWindow", " Hello I am Here To Help You"))
        self.label_6.setText(_translate("MainWindow", " You Can Ask me About"))
        self.label_3.setText(_translate("MainWindow", "Time, Date, Day"))
        self.label_4.setText(_translate("MainWindow", " Weather , Temperature of any City "))
        self.label_5.setText(_translate("MainWindow", "Some General Questions "))
        self.label.setText(_translate("MainWindow", " You "))
        self.label_7.setText(_translate("MainWindow", " Tulip "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
