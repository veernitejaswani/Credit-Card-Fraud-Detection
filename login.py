# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cfd import *
import MySQLdb as mdb

class Ui_MainWindow(object):
    xuname = ''
    def cfdshow(self):
        self.welcomeWindow = QtWidgets.QMainWindow()
        self.ui = cfdclass()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

    def validate(self):

        uname = self.lineEdit.text()
        pwd = self.lineEdit_2.text()

        con = mdb.connect("localhost", "raja", "raja", "testing", 3308)
        cur = con.cursor()
        cur.execute("SELECT * FROM users where id='" + uname +"';" )
        for i in range(cur.rowcount):
            result = cur.fetchall()
            for row in result:
                xuname = (str(row[1]))
                xpwd = (str(row[2]))

        print(xuname)
        print(xpwd)

        if (uname==xuname and pwd==xpwd):
            open('log.txt', 'w').close()

            with open('log.txt', 'w') as file:
                file.write(uname)
                file.close()
            self.cfdshow()
        else:
            self.invalid.show()





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 171, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 210, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 290, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.validate)
        self.invalid = QtWidgets.QLabel(self.centralwidget)
        self.invalid.hide()
        self.invalid.setGeometry(QtCore.QRect(190, 260, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.invalid.setFont(font)
        self.invalid.setStyleSheet("color: rgb(255, 0, 0);")
        self.invalid.setObjectName("invalid")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Credit Card Fraud Detection"))
        self.label_2.setText(_translate("MainWindow", "User ID"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.invalid.setText(_translate("MainWindow", "Invalid credentials"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

