# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cfd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb

class cfdclass(object):


    def updateThresholds(self):
        con = mdb.connect("localhost", "raja", "raja", "testing", 3308)
        xact = self.actno.text()
        cur = con.cursor()
        cur.execute("UPDATE thresholds SET  maxlimit = '" + self.lineEdit1.text() + "' where accountno='" + xact + "';")
        cur.execute("UPDATE thresholds SET  shopping = '" + self.lineEdit2.text() + "' where accountno='" + xact + "';")
        cur.execute("UPDATE thresholds SET  travel = '" + self.lineEdit3.text() + "' where accountno='" + xact + "';")
        cur.execute("UPDATE thresholds SET  bills = '" + self.lineEdit4.text() + "' where accountno='" + xact + "';")
        cur.execute("UPDATE thresholds SET  misc = '" + self.lineEdit5.text() + "' where accountno='" + xact + "';")


    def resetThresholds(self):
        self.lineEdit1.setText("0")
        self.lineEdit2.setText("0")
        self.lineEdit3.setText("0")
        self.lineEdit4.setText("0")
        self.lineEdit5.setText("0")


    def loadThresholds(self):
        con = mdb.connect("localhost", "raja", "raja", "testing", 3308)
        cur = con.cursor()
        xact = self.actno.text()
        cur.execute("SELECT * FROM thresholds where accountno ='"+xact+"';")

        for i in range(cur.rowcount):
            result = cur.fetchall()

            rew = 0
            for row in result:
                self.lineEdit1.setText((str(row[1])))
                self.lineEdit2.setText((str(row[2])))
                self.lineEdit3.setText((str(row[3])))
                self.lineEdit4.setText((str(row[4])))
                self.lineEdit5.setText((str(row[5])))
                rew = rew + 1



    def loadTransactionTable(self):
        self.loadThresholds()
        con = mdb.connect("localhost", "raja", "raja", "testing", 3308)
        cur = con.cursor()
        cur.execute("SELECT * FROM check1")

        for i in range(cur.rowcount):
            result = cur.fetchall()

            rew = 0
            for row in result:
                self.tableWidget.setItem(rew, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(rew, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableWidget.setItem(rew, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(rew, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                rew = rew + 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(500, 50, 530, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 20, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 310, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 350, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(110, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setText("")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(110, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setText("")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(110, 260, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit3.setFont(font)
        self.lineEdit3.setText("")
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(110, 300, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit4.setFont(font)
        self.lineEdit4.setText("")
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(110, 340, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit5.setFont(font)
        self.lineEdit5.setText("")
        self.lineEdit5.setObjectName("lineEdit5")
        self.applybt = QtWidgets.QPushButton(self.centralwidget)
        self.applybt.setGeometry(QtCore.QRect(70, 440, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.applybt.setFont(font)
        self.applybt.setObjectName("applybt")
        self.applybt.clicked.connect(self.updateThresholds)                                # UPDATING THRESHOLDS
        self.resetbt = QtWidgets.QPushButton(self.centralwidget)
        self.resetbt.setGeometry(QtCore.QRect(180, 440, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resetbt.setFont(font)
        self.resetbt.setObjectName("resetbt")
        self.resetbt.clicked.connect(self.resetThresholds)
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.clicked.connect(self.loadTransactionTable)                                # LOAD TABLE FUNCTION CALL
        self.refresh.setGeometry(QtCore.QRect(710, 600, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.refresh.setFont(font)
        self.refresh.setObjectName("refresh")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.actno = QtWidgets.QLabel(self.centralwidget)
        self.actno.setGeometry(QtCore.QRect(180, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actno.setFont(font)
        self.actno.setObjectName("actno")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 20, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        with open('log.txt') as f:
            first_line = f.readline()
            f.close()

        con = mdb.connect("localhost", "raja", "raja", "testing", 3308)
        cur = con.cursor()
        cur.execute("SELECT accountno FROM users where id='" + first_line + "';")
        for i in range(cur.rowcount):
            result = cur.fetchall()
            for row in result:
                actnumber = (str(row[0]))

        self.actno.setText(actnumber)

        self.loadThresholds()
        self.loadTransactionTable()





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "User Defined Thresholds"))
        self.label_2.setText(_translate("MainWindow", "Max Limit"))
        self.label_3.setText(_translate("MainWindow", "Shopping"))
        self.label_4.setText(_translate("MainWindow", "Travel"))
        self.label_5.setText(_translate("MainWindow", "Bills"))
        self.label_6.setText(_translate("MainWindow", "Misc."))
        self.applybt.setText(_translate("MainWindow", "APPLY"))
        self.resetbt.setText(_translate("MainWindow", "RESET"))
        self.refresh.setText(_translate("MainWindow", "REFRESH"))
        self.label_7.setText(_translate("MainWindow", "Account Number:"))
        self.actno.setText(_translate("MainWindow", "01234567890"))
        self.label_9.setText(_translate("MainWindow", "Transactions History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = cfdclass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print(login.uname)
    sys.exit(app.exec_())

