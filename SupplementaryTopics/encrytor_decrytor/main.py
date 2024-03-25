# main.py

import sys
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap

class ImageEncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Encryption and Decryption")
        self.setGeometry(100, 100, 800, 600)


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.input_label = QLabel("Input Image: encrytor_decrytor/ashkan.original.jpg")
        self.input_image_label = QLabel()
        input_image_path = "encrytor_decrytor/ashkan.original.jpg"
        input_pixmap = QPixmap(input_image_path)
        desired_width= 100
        desired_height = 130
        input_pixmap = input_pixmap.scaled(desired_width, desired_height, aspectMode=Qt.KeepAspectRatio)
        self.input_image_label.setPixmap(input_pixmap)

        self.encrypted_label = QLabel("Encrypted Image: encrytor_decrytor/encrypted_image.bmp")
        self.encrypted_image_label = QLabel()
        encrypted_image_path = "encrytor_decrytor/encrypted_image.bmp"
        encrypted_pixmap = QPixmap(encrypted_image_path)
        desired_width= 100
        desired_height = 130
        encrypted_pixmap = encrypted_pixmap.scaled(desired_width, desired_height, aspectMode=Qt.KeepAspectRatio)
        self.encrypted_image_label.setPixmap(encrypted_pixmap)

        self.decrypted_label = QLabel("Decrypted Image: encrytor_decrytor/decrypted_image.jpg")
        self.decrypted_image_label = QLabel()
        decrypted_image_path = "encrytor_decrytor/decrypted_image.jpg"
        decrypted_pixmap = QPixmap(decrypted_image_path)
        desired_width= 100
        desired_height = 130
        decrypted_pixmap = decrypted_pixmap.scaled(desired_width, desired_height, aspectMode=Qt.KeepAspectRatio)
        self.decrypted_image_label.setPixmap(decrypted_pixmap)


        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_image_label)

        self.layout.addWidget(self.encrypted_label)
        self.layout.addWidget(self.encrypted_image_label)

        self.layout.addWidget(self.decrypted_label)
        self.layout.addWidget(self.decrypted_image_label)

        self.central_widget.setLayout(self.layout)

        # Connect buttons and load images here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEncryptionApp()
    window.show()
    sys.exit(app.exec())
