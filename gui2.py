# https://touch-sp.hatenablog.com/entry/2021/06/11/230615

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import rospy
import tf

X = 0
Y = 0
Z = 0
EX = 0
EY = 0
EZ = 0

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        
        self.angle_label = [QLabel() for x in range(6)]

        for each_label in self.angle_label:
            each_label.setText(str(0))

        self.angle_slider = [QSlider(Qt.Orientation.Horizontal) for x in range(6)]
        
        for each_slider in self.angle_slider:
            each_slider.setMaximum(10)
            each_slider.setMinimum(-10)
            each_slider.setValue(0)
            each_slider.valueChanged.connect(self.value_change)
        
        servo_frame = [QFrame() for x in range(6)]
        servo_layout = [QHBoxLayout() for x in range(6)]

        vbox = QVBoxLayout()

        for i in range(6):
            servo_layout[i].addWidget(self.angle_label[i])
            servo_layout[i].addWidget(self.angle_slider[i])

            servo_frame[i].setLayout(servo_layout[i])
            vbox.addWidget(servo_frame[i])  
            
        self.setLayout(vbox)
        self.setGeometry(300, 300, 450, 300)
        self.show()
    
    def value_change(self):
        global X,Y,Z
        global EX,EY,EZ
        for i in range(6):
            self.angle_label[i].setText(str(self.angle_slider[i].value()))

        X = self.angle_slider[0].value()
        Y = self.angle_slider[1].value()
        Z = self.angle_slider[2].value()
        EX = self.angle_slider[3].value()
        EY = self.angle_slider[4].value()
        EZ = self.angle_slider[5].value()


rospy.init_node('tf_publisher_gui')
br = tf.TransformBroadcaster()

app = QApplication(sys.argv)
ex =Window()

r = rospy.Rate(10)
while not rospy.is_shutdown():
    QApplication.processEvents()

    br.sendTransform(( X, Y, Z),
                     tf.transformations.quaternion_from_euler(EX, EY, EZ),
                     rospy.Time.now(),
                     "base_link",
                     "world")

    r.sleep()
