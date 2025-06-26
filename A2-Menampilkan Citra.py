import sys
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

class ShowImage(QMainWindow):
    def __init__(self):
        super(ShowImage, self).__init__()
        loadUi('GUI.ui', self) 
        self.Image = None 
        
        self.button_LoadCitra.clicked.connect(self.fungsi)

    def fungsi(self):
        self.Image = cv2.imread('Informasi-kesehatan.jpg')
        
        if self.Image is None:
            print("Gambar tidak ditemukan!")
            return
        
        self.Image = cv2.cvtColor(self.Image, cv2.COLOR_BGR2RGB) 
        self.displayImage()

    def displayImage(self):
        qformat = QImage.Format_RGB888 

        img = QImage(self.Image.data, self.Image.shape[1], self.Image.shape[0],
                     self.Image.strides[0], qformat)
        img = img.rgbSwapped()

        self.label.setPixmap(QPixmap.fromImage(img))
        self.label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShowImage()
    window.show()
    sys.exit(app.exec_())
