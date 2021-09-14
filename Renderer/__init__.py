from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import xml.etree.ElementTree as ET
import sys

from Renderer.SubRenderers.text_render import ColoredText
from Renderer.SubRenderers.graph_render import GraphPainter
from Renderer.SubRenderers.label_render import LabelRender
from common.singleton import singleton


render_tags = {
    "text": ColoredText,
    "graph": GraphPainter
}


class Renderer(QObject):
    render = pyqtSignal(QFormLayout, ET.Element)
    instance = None

    def __init__(self):
        super().__init__()
        Renderer.instance = self
        self.render.connect(self.run)

    # @pyqtSlot
    def run(self, layout, data):
        for i in range(len(layout)):
            layout.removeRow(i)
        for child in data:
            # print(child.tag)
            layout.addRow(render_tags[child.tag](child))


def render(layout: QFormLayout, data: ET.Element):
    for i in range(len(layout)):
        layout.removeRow(i)
    for child in data:
        # print(child.tag)
        layout.addRow(render_tags[child.tag](child))


if __name__ == '__main__':
    class MainWindow(QWidget):  # главное окно
        def __init__(self, parent=None):
            super().__init__(parent)
            # self.form = QFormLayout()
            self.setupUi()

        def setupUi(self):
            self.setWindowTitle("Hello, world")  # заголовок окна
            self.setStyleSheet("background-color: black")
            self.move(300, 300)  # положение окна
            self.resize(200, 200)  # размер окна
            # self.lbl = QLabel('Hello, world!!!', self)
            self.form = QFormLayout()
            # self.form.addRow(QLabel("hello"))
            self.setLayout(self.form)
            self.show()

    root = ET.Element("root")
    text1 = ET.SubElement(root, "text")
    ET.SubElement(text1, "sub_text", color="red").text = "abc"
    ET.SubElement(text1, "sub_text", color="blue").text = "def"
    ET.SubElement(text1, "sub_text", color="lightblue").text = "123"
    ET.SubElement(text1, "sub_text", color="white").text = "123"
    text2 = ET.SubElement(root, "text")
    ET.SubElement(text2, "sub_text", color="white").text = "hello"
    ET.SubElement(text2, "sub_text", color="pink").text = "world"
    ET.SubElement(text2, "sub_text", color="green").text = "псы"
    ET.SubElement(root, "graph").text = "12 55 17 66 25 77 28 88"

    app = QApplication(sys.argv)
    win = MainWindow()
    render(win.form, root)
    win.show()
    sys.exit(app.exec_())