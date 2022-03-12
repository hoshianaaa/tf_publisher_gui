# https://touch-sp.hatenablog.com/entry/2021/06/11/230615

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        
        self.angle_label = [QLabel() for x in range(4)]

        for each_label in self.angle_label:
            each_label.setText(str(90))

        self.angle_slider = [QSlider(Qt.Orientation.Horizontal) for x in range(4)]
        
        for each_slider in self.angle_slider:
            each_slider.setMaximum(170)
            each_slider.setMinimum(10)
            each_slider.setValue(90)
            each_slider.valueChanged.connect(self.value_change)
        
        servo_frame = [QFrame() for x in range(4)]
        servo_layout = [QHBoxLayout() for x in range(4)]

        vbox = QVBoxLayout()

        for i in range(4):
            servo_layout[i].addWidget(self.angle_label[i])
            servo_layout[i].addWidget(self.angle_slider[i])

            servo_frame[i].setLayout(servo_layout[i])
            vbox.addWidget(servo_frame[i])  
            
        self.setLayout(vbox)
        self.setGeometry(300, 300, 450, 300)
        self.show()
    
    def value_change(self):
        for i in range(4):
            self.angle_label[i].setText(str(self.angle_slider[i].value()))

app = QApplication(sys.argv)
ex =Window()

sys.exit(app.exec())
