
import sys
import os
import pydicom
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QSlider, QTextBrowser, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap


class VentanaBase(QMainWindow):
    def __init__(self, ui_file):
        super(VentanaBase, self).__init__()
        loadUi(ui_file, self)

class SistemaVentana(VentanaBase):
    def __init__(self):
        super(SistemaVentana, self).__init__("VentanaP.ui")
        self.Boton_Usuario.clicked.connect(self.mostrar_login)

    def mostrar_login(self):
        self.hide()
        login_ventana.mostrar_ventana()

    def mostrar_ingreso(self):
        ingreso_ventana.show()

class LoginVentana(VentanaBase):
    def __init__(self):
        super(LoginVentana, self).__init__("Ventana2.ui")
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.salir)

    def mostrar_ventana(self):
        self.show()

    def login(self):
        usuario = self.lineEdit.text()
        contraseña = self.lineEdit_2.text()
        if len(usuario) == 0 or len(contraseña) == 0:
            self.label_6.setText("Por favor ingrese todos los datos")
        elif usuario == "medicoAnalitico" and contraseña == "bio12345":
            self.hide()
            sistema_ventana.mostrar_ingreso()
            
        else:
            self.hide()
            error_ventana.mostrar_ventana()

    def salir(self):
        self.hide()
        sistema_ventana.show()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.label_6.clear()

class IngresoVentana(VentanaBase):
    def __init__(self):
        super(IngresoVentana, self).__init__("Ventana3.ui")
        self.pushButton.clicked.connect(self.continuar_ingreso)
        self.pushButton_2.clicked.connect(self.salir)

    def continuar_ingreso(self):
        self.hide()
        login_ventana.limpiar_campos()
        ventana_img.show()

    def salir(self):
        sistema_ventana.show()
        login_ventana.limpiar_campos()

class ErrorVentana(VentanaBase):
    def __init__(self):
        super(ErrorVentana, self).__init__("Ventana4.ui")
        self.pushButton.clicked.connect(self.regresar_error)

    def mostrar_ventana(self):
        self.show()

    def regresar_error(self):
        login_ventana.limpiar_campos()
        self.hide()
        login_ventana.mostrar_ventana()

class VentanaImg(VentanaBase):
    def __init__(self):
        super(VentanaImg, self).__init__("VentanaImg.ui")
        self.label_imagen = self.findChild(QLabel, 'label')
        self.textBrowser_info = self.findChild(QTextBrowser, 'textBrowser')
        self.horizontalSlider = self.findChild(QSlider, 'horizontalSlider')
        self.pushButton_cargar_imagenes = self.findChild(QPushButton, 'pushButton')
        self.pushButton_2 = self.findChild(QPushButton, 'pushButton_2')
        self.pushButton_3 = self.findChild(QPushButton, 'pushButton_3')
        self.pushButton_4 = self.findChild(QPushButton, 'pushButton_4')

        if self.pushButton_4 is not None:
            self.pushButton_4.clicked.connect(self.regresar_a_ventana_base)
        else:
            print("")

        if self.pushButton_cargar_imagenes is not None:
            self.pushButton_cargar_imagenes.clicked.connect(self.cargar_imagenes)
        else:
            print("")

        if self.pushButton_2 is not None:
            self.pushButton_2.clicked.connect(self.regresar_imagen)
        else:
            print("")

        if self.pushButton_3 is not None:
            self.pushButton_3.clicked.connect(self.siguiente_imagen)
        else:
            print("")

        if self.horizontalSlider is not None:
            self.horizontalSlider.valueChanged.connect(self.slider_cambio_valor)

        self.current_index = 0
        self.folder_path = ""
        self.image_files = []

    def cargar_imagenes(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta", "")
        if self.folder_path:
            self.image_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith('.dcm')]
            if self.image_files:
                self.mostrar_imagen(self.current_index)
                self.actualizar_info_paciente(os.path.join(self.folder_path, self.image_files[self.current_index]))
                self.horizontalSlider.setRange(0, len(self.image_files) - 1)

    def mostrar_imagen(self, index):
        if 0 <= index < len(self.image_files):
            image_path = os.path.join(self.folder_path, self.image_files[index])
            dicom_data = pydicom.dcmread(image_path)
            image_array = dicom_data.pixel_array
            qimage = QImage(image_array.data, image_array.shape[1], image_array.shape[0], image_array.shape[1] * image_array.itemsize, QImage.Format_Grayscale8)
            qimage = qimage.copy()  
            pixmap = QPixmap.fromImage(qimage)
            self.label_imagen.setPixmap(pixmap)
            self.horizontalSlider.setValue(index)

    def actualizar_info_paciente(self, image_path):
        dicom_data = pydicom.dcmread(image_path)
        info_text = f"Paciente: {dicom_data.PatientName}\n" \
                    f"ID Paciente: {dicom_data.PatientID}\n" \
                    f"Fecha de Nacimiento: {dicom_data.PatientBirthDate}\n" \
                    f"Sexo: {dicom_data.PatientSex}\n" \
                    f"Modalidad: {dicom_data.Modality}\n"
        self.textBrowser_info.setPlainText(info_text)

    def regresar_imagen(self):
        self.current_index = max(0, self.current_index - 1)
        self.mostrar_imagen(self.current_index)
        self.actualizar_info_paciente(os.path.join(self.folder_path, self.image_files[self.current_index]))

    def siguiente_imagen(self):
        self.current_index = min(len(self.image_files) - 1, self.current_index + 1)
        self.mostrar_imagen(self.current_index)
        self.actualizar_info_paciente(os.path.join(self.folder_path, self.image_files[self.current_index]))

    def slider_cambio_valor(self, value):
        self.current_index = value
        self.mostrar_imagen(self.current_index)

    def regresar_a_ventana_base(self):
        self.hide()
        sistema_ventana.show()
    
# Inicialización de las ventanas
app = QApplication(sys.argv)
sistema_ventana = SistemaVentana()
login_ventana = LoginVentana()
ingreso_ventana = IngresoVentana()
error_ventana = ErrorVentana()
ventana_img = VentanaImg()

# Conexiones con botones
sistema_ventana.show()
sys.exit(app.exec_())
