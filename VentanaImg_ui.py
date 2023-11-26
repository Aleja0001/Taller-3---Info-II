# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaImg.ui'
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
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 51, 51);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 70, 491, 321))
        self.label.setStyleSheet(u"background-color: rgb(205, 255, 239);\n"
"border-radius:10px;")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(190, 400, 431, 31))
        self.horizontalSlider.setStyleSheet(u"background-color: rgb(217, 145, 0);\n"
"border-bottom-color: rgb(6, 6, 6);\n"
"border-radius:10px;")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 400, 71, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(210, 255, 225);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px; \n"
"padding: 6px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 681, 41))
        font = QFont()
        font.setFamilies([u"Swis721 Cn BT"])
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(199, 247, 173);\n"
"border-radius:20px;")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(380, 450, 91, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(210, 255, 225);\n"
"background-color: rgb(0, 147, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 10px;")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 180, 141, 101))
        self.textBrowser.setStyleSheet(u"background-color: rgb(205, 255, 239);\n"
"border-radius:10px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 141, 21))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 241, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;\n"
"border-radius:10px;\n"
" ")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 400, 71, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(210, 255, 225);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px; \n"
"padding: 6px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#003300;\"> VISUALIZACI\u00d3N DE IM\u00c1GENES M\u00c9DICAS</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cargar Carpeta", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Siguiente", None))
    # retranslateUi

