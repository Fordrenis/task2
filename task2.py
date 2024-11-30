import sys
import io
import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtCore import Qt

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>280</x>
      <y>50</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Нарисовать</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>100</y>
      <width>651</width>
      <height>451</height>
     </rect>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 0), Qt.BrushStyle.SolidPattern))

        for circle in self.circles:
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def add_circle(self):
        x = random.randint(0, self.width() - 50)
        y = random.randint(0, self.height() - 50)
        diameter = random.randint(10, 100)
        self.circles.append((x, y, diameter))
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.setGeometry(100, 100, 800, 600)

        self.circle_drawer = CircleDrawer()

        layout = QVBoxLayout()
        layout.addWidget(self.circle_drawer)

        self.pushButton.clicked.connect(self.circle_drawer.add_circle)
        layout.addWidget(self.pushButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())