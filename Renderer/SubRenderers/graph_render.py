
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QPolygon
from PyQt5.QtCore import Qt, QPoint, QRectF, QEvent
import xml.etree.ElementTree as ET

class GraphPainter(QWidget):
    def __init__(self, data: ET.Element):
        super().__init__()

        self.data = data
        self.initUI()

    def initUI(self):

        # label = QLabel("test", self)
        # label.move(0, 0)
        self.setMinimumHeight(100)
        # self.show()
        pass

    def paintEvent(self, event):
        graph = QPainter(self)

        graph.setPen(Qt.GlobalColor.red)

        values = [int(i) for i in self.data.text.split()]
        x_step = self.width() // len(values)
        y_last = values[0]
        for i, y in enumerate(values):
            graph.drawLine(i * x_step, 100 - y_last, (i + 1) * x_step, 100 - y)
            y_last = y
