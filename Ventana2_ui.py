# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import imagenes1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 260)
        MainWindow.setMinimumSize(QSize(400, 260))
        MainWindow.setMaximumSize(QSize(400, 260))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 51, 51);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 21))
        self.label.setStyleSheet(u"background-color: rgb(199, 247, 173);\n"
"border-radius:  10px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 391, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 80, 71, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 130, 111, 21))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 80, 171, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(192, 255, 169);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 190, 111, 31))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(210, 255, 225);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px; \n"
"padding: 6px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 210, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(210, 255, 225);\n"
"background-color: rgb(0, 147, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 120, 171, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(192, 255, 169);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 80, 61, 31))
        self.label_5.setStyleSheet(u"image: url(:/img/1564535_customer_user_userphoto_account_person_icon.png);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 160, 241, 21))
        self.label_6.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 51, 51);\n"
"color:red;\n"
"border-radius: 8px;")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 120, 41, 31))
        self.label_7.setStyleSheet(u"border-image: url(:/img/622405_lock_security_password_protect_safety_icon.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#003300;\">SISTEMA PARA LA VISUALIZACI\u00d3N DE IM\u00c1GENES M\u00c9DICAS</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Por favor ingrese su Usuario y Contrase\u00f1a para ingresar al sistema</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Usuario:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Contrase\u00f1a:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"salir", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
    # retranslateUi

