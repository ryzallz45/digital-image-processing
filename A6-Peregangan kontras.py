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
        self.button_prosesCitra.clicked.connect(self.stretching)
        self.actionContrast_Stretching.triggered.connect(self.stretching)
        
    def fungsi(self):
        self.Image = cv2.imread('man.jpg')
        
        if self.Image is None:
            print("Gambar tidak ditemukan!")
            return
        
        self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB) 
        self.displayImage(self.Image, self.label)

    def stretching(self):
        if self.Image is None:
            print("Belum ada gambar yang dimuat!")
            return

        minV = np.min(self.Image)
        maxV = np.max(self.Image)
    
        self.Image = ((self.Image - minV) / (maxV - minV) * 255).astype(np.uint8)
    
        self.displayImage(self.Image, self.label_2)
                  
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
