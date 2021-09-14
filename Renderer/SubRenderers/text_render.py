from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QWidget, QLabel
import xml.etree.ElementTree as ET


class ColoredText(QWidget):

    padding = 15

    def __init__(self, data: ET.Element):
        super().__init__()

        self.initUI(data)

    def initUI(self, data: ET.Element):
        cur_y = 0
        cur_x = 0
        font = QFont("Courier", 15)
        fm = QFontMetrics(font)
        # print(self.window().width(), self.width())
        for child in data:
            if child.tag == "enter":
                cur_x = 0
                cur_y += fm.height()
                continue
            # print("width", self.width())
            for word in child.text.split():
                if cur_x + fm.width(word) > self.width():
                    cur_x = 0
                    cur_y += fm.height()
                label = QLabel(word, self)
                label.setFont(font)
                # print(child.attrib["color"])

                color = None
                if "color" in child.attrib.keys():
                    color = child.attrib["color"]
                else:
                    color = "white"

                label.setStyleSheet("color:" + color)
                label.move(cur_x, cur_y)
                cur_x += fm.width(word + " ")

        self.setMinimumHeight(cur_y + fm.height())
        # self.show()

