import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import rospy

def window():
  rospy.init_node("PyQT5_ROS")
  app = QApplication(sys.argv)
  w = QWidget()
  b = QLabel(w)
  w.setGeometry(100,100,200,50)
  b.setText("         ")
  b.move(50,20)
  w.setWindowTitle("PyQt5 + ROS")
  w.show()

  count = 0
  while not rospy.is_shutdown():
    QApplication.processEvents()
    b.setText(str(count))
    count = count + 1

if __name__ == '__main__':
   window()
