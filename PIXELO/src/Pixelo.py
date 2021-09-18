# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 13:03:06 2021

@author: junob
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:16:18 2021

@author: junob
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

import img2pixel

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("../ui/pixelo.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_file.triggered.connect(self.loadFile)
        self.save.triggered.connect(self.saveFile)
        self.information.triggered.connect(self.information_dialog_open)
        
        self.input_img, self.size, self.colors = self.load_config()
        self.sizeSlider.setValue(self.size)
        self.colorsSlider.setValue(self.colors)
        self.sizeSlider.valueChanged.connect(self.save_config)
        self.colorsSlider.valueChanged.connect(self.save_config)
        
        fig = plt.Figure()
        self.ax = fig.add_subplot(111)
        self.ax.axes.xaxis.set_visible(False)
        self.ax.axes.yaxis.set_visible(False)
        self.canvas = FigureCanvas(fig)
        self.graph_verticalLayout.addWidget(self.canvas)
        try:
            pixel_img = img2pixel.img2pixel(self.input_img, self.size/100, self.colors)
        except:
            self.input_img ='../img/Lenna.png'
            pixel_img = img2pixel.img2pixel(self.input_img, self.size/100, self.colors)         
        self.ax.imshow(pixel_img, interpolation='nearest')
        self.canvas.draw()
        
        self.lbl_img = QLabel()
        self.lbl_img.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(self.input_img)
        self.lbl_img.setPixmap(pixmap)
        self.graph_verticalLayout_0.addWidget(self.lbl_img)

    def show_input_image(self):
        pixmap = QPixmap(self.input_img)
        self.lbl_img.setPixmap(pixmap)
        #self.graph_verticalLayout_0.addWidget(self.lbl_img)
        
    def load_config(self):
        with open("../config/Pixelo.conf", "r", -1, 'utf-8') as f:
            str_input_img, str_size, str_colors = f.readlines()
        return str_input_img.replace('\n', ''), int(str_size), int(str_colors)

    def save_config(self):
        self.size = self.sizeSlider.value()
        self.colors = self.colorsSlider.value()
        with open("../config/Pixelo.conf", "w", -1, 'utf-8') as f:
            f.write(self.input_img +'\n' + str(self.size) + '\n' + str(self.colors))
        pixel_img = img2pixel.img2pixel(self.input_img, self.size/100, self.colors)
        self.ax.imshow(pixel_img, interpolation='nearest')
        self.canvas.draw()
        
    def loadFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '',
                                        'Image File(*.png *.jpg, *jpeg);; All File(*)')[0]        
        if not filename == '':
            self.input_img = filename
        self.show_input_image()
        self.save_config()
        
    def saveFile(self):
        save_img_name = QFileDialog.getSaveFileName(self, 'Save File', '',
                                        'Image File(*.png *.jpg, *jpeg);; All File(*)')[0]
        if not save_img_name == '':
            pixel_img = img2pixel.img2pixel(self.input_img, self.size/100, self.colors)
            plt.imsave(save_img_name, pixel_img)

    def information_dialog_open(self):
        dialog = InformationDialog()
        dialog.exec_()
        
information_dialog = uic.loadUiType("../ui/Information.ui")[0]
class InformationDialog(QDialog, information_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()