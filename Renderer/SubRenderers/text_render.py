
from PyQt5.QtWidgets import QWidget, QLabel
import xml.etree.ElementTree as ET

class ColoredText(QWidget):

    padding = 15

    def __init__(self, data: ET.Element):
        super().__init__()

        self.initUI(data)

    def initUI(self, data: ET.Element):
        cur_y = 0
        # self.label1 = QLabel("1234235", self)
        # self.label1.move(0, 0)
        for child in data:
            label = QLabel(child.text, self)
            print(child.attrib["color"])
            label.setStyleSheet("color:" + child.attrib["color"])
            label.move(0, cur_y)
            print(label.font().weight())

            cur_y += self.padding
        self.setMinimumHeight(cur_y)
        self.show()

