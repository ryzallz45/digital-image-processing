import sys
import cv2
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('GUI2.ui', self) 
        self.Image = None 
        self.button_LoadCitra.clicked.connect(self.fungsi)
        self.button_prosesCitra.clicked.connect(self.grayscale)
        self.actionBrightness.triggered.connect(self.brightness)
        
    def fungsi(self):
        self.Image = cv2.imread('Informasi-kesehatan.jpg')
        
        if self.Image is None:
            print("Gambar tidak ditemukan!")
            return
        
        self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB) 
        self.displayImage(self.Image, self.label)
        
    def grayscale(self):
        if self.Image is None:
            print("Belum ada gambar yang dimuat!")
            return

        H, W = self.Image.shape[:2]
        gray = np.zeros((H, W), np.uint8)
        for i in range(H):
            for j in range(W):
                gray[i, j] = np.clip(0.299 * self.Image[i, j, 0] +
                                     0.587 * self.Image[i, j, 1] +
                                     0.114 * self.Image[i, j, 2], 0, 255)
        self.displayImage(gray, self.label_2)

    def brightness(self):
        if self.Image is None:
            print("Belum ada gambar yang dimuat!")
            return

        H, W, C = self.Image.shape  
        bright_image = np.zeros((H, W, C), np.uint8)
        brightness = 70 

        for i in range(H):
            for j in range(W):
                for c in range(C): 
                    pixel_value = int(self.Image[i, j, c]) + brightness 
                    bright_image[i, j, c] = np.clip(pixel_value, 0, 255) 

        self.displayImage(bright_image, self.label_2)

    def displayImage(self, image, label):
        if image is None:
            return

        if len(image.shape) == 2:
            qformat = QImage.Format_Grayscale8
        else: 
            qformat = QImage.Format_RGB888
        
        img = QImage(image.data, image.shape[1], image.shape[0],
                     image.strides[0], qformat)
        
        label.setPixmap(QPixmap.fromImage(img))
        label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())
