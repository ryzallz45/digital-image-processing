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
        self.button_prosesCitra.clicked.connect(self.negatif)
        self.actionNegative_Image.triggered.connect(self.negatif)
        
    def fungsi(self):
        self.Image = cv2.imread('12.jpg')
        
        if self.Image is None:
            print("Gambar tidak ditemukan!")
            return
        
        self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB) 
        self.displayImage(self.Image, self.label)

    def negatif(self):
        if self.Image is None:
            print("Belum ada gambar yang dimuat!")
            return

        self.Image = 255 - self.Image
        
        self.displayImage(self.Image, self.label_2)
        self.repaint() 
    
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
        QtWidgets.QApplication.processEvents() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())