# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 21, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 10, 21, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 10, 21, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 10, 114, 31))
        self.pushButton.setObjectName("pushButton")
        self.ode = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ode.setGeometry(QtCore.QRect(50, 10, 191, 21))
        self.ode.setObjectName("ode")
        self.x0 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.x0.setGeometry(QtCore.QRect(270, 10, 41, 21))
        self.x0.setObjectName("x0")
        self.y0 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.y0.setGeometry(QtCore.QRect(340, 10, 41, 21))
        self.y0.setObjectName("y0")
        self.xn = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.xn.setGeometry(QtCore.QRect(420, 10, 41, 21))
        self.xn.setObjectName("xn")
        self.xk = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.xk.setGeometry(QtCore.QRect(490, 10, 51, 21))
        self.xk.setObjectName("xk")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "y\'="))
        self.label_2.setText(_translate("MainWindow", "y("))
        self.label_3.setText(_translate("MainWindow", ")="))
        self.label_4.setText(_translate("MainWindow", "xn"))
        self.label_5.setText(_translate("MainWindow", "xk"))
        self.pushButton.setText(_translate("MainWindow", "calculate"))
        self.xn.setPlainText(_translate("MainWindow", "-5"))
        self.xk.setPlainText(_translate("MainWindow", "5"))

