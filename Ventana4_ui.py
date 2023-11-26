# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana4.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMinimumSize(QSize(400, 200))
        MainWindow.setMaximumSize(QSize(400, 200))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 51, 51);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 21))
        self.label.setStyleSheet(u"background-color: rgb(199, 247, 173);\n"
"border-radius:  10px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 130, 131, 31))
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
        self.pushButton_2.setGeometry(QRect(300, 190, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(210, 255, 225);\n"
"background-color: rgb(0, 147, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 361, 61))
        self.label_2.setStyleSheet(u"background-color: rgb(205, 255, 239);\n"
"border-radius:10px;")
        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"salir", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#005500;\">Los datos ingreasos NO son correctos </span></p><p align=\"center\"><span style=\" font-size:11pt; color:#005500;\">Intente nuevamente</span></p></body></html>", None))
    # retranslateUi

