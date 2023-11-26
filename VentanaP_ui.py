# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VentanaP.ui'
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
import imagenes_rc

class Ui_VentanaP(object):
    def setupUi(self, VentanaP):
        if not VentanaP.objectName():
            VentanaP.setObjectName(u"VentanaP")
        VentanaP.resize(600, 400)
        VentanaP.setMinimumSize(QSize(600, 400))
        VentanaP.setMaximumSize(QSize(600, 400))
        VentanaP.setStyleSheet(u"background-color: rgb(0, 51, 51);")
        self.centralwidget = QWidget(VentanaP)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 581, 41))
        font = QFont()
        font.setFamilies([u"Swis721 Cn BT"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(199, 247, 173);\n"
"border-radius:20px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 90, 501, 301))
        self.label_2.setStyleSheet(u"border-image: url(:/imagenes/Imagenes.jpg);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 40, 51, 51))
        self.label_3.setStyleSheet(u"border-image: url(:/imagenes/285641_id_user_icon.png);")
        self.Boton_Usuario = QPushButton(self.centralwidget)
        self.Boton_Usuario.setObjectName(u"Boton_Usuario")
        self.Boton_Usuario.setGeometry(QRect(140, 50, 331, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.Boton_Usuario.setFont(font1)
        self.Boton_Usuario.setStyleSheet(u"background-color: rgb(255, 255, 204);\n"
"border-radius:10px;")
        VentanaP.setCentralWidget(self.centralwidget)
        self.Boton_Usuario.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.menubar = QMenuBar(VentanaP)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 21))
        VentanaP.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaP)
        self.statusbar.setObjectName(u"statusbar")
        VentanaP.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaP)

        QMetaObject.connectSlotsByName(VentanaP)
    # setupUi

    def retranslateUi(self, VentanaP):
        VentanaP.setWindowTitle(QCoreApplication.translate("VentanaP", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("VentanaP", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#003300;\">SISTEMA PARA LA VISUALIZACI\u00d3N DE IM\u00c1GENES M\u00c9DICAS</span></p></body></html>", None))
        self.label_2.setText("")
        self.label_3.setText("")
#if QT_CONFIG(tooltip)
        self.Boton_Usuario.setToolTip(QCoreApplication.translate("VentanaP", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.Boton_Usuario.setText(QCoreApplication.translate("VentanaP", u"        Ingresar con Usuario y Contrase\u00f1a", None))
    # retranslateUi

