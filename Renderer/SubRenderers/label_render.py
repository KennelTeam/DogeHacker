from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QWidget, QLabel
import xml.etree.ElementTree as ET

class LabelRender(QWidget):

    def __init__(self, data: ET.Element):
        super().__init__()
        self.data = data
        # self.data = "<font color=yellow>yellow </font><font color=red>red </font><font color=blue>blue</font>"
        self.data = "<font color=white>aabc fdgkjrt</font><font color=yellow> dggr fg rger sdfd</font>"

        self.initUI()

    def initUI(self):
        self.label = QLabel(self.data, self)
        self.label.setWordWrap(True)
        self.setMinimumHeight(self.label.height() * 2)

    def paintEvent(self, event):


        # print(self.width())
        # self.label.setMinimumWidth(self.width())
        self.label.setFixedWidth(self.width())
        self.label.setScaledContents(True)
        # self.label.setMinimumHeight(self.label.height())
        # print(">>", self.label.width(), self.label.height())