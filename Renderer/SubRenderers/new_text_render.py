import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import *

class NewTextRender(QWidget):
    textEdit: QTextEdit

    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit(self)
        self.textEdit.setHtml('''
            <h1>Wellcome!</h1>
        ''')

    def updateData(self, data: ET.ElementTree):
        self.textEdit.clear()
        for el in data:
            text = el.text
            
            if el.tag == 'enter':
                text = '<br>'

            if text is None:
                continue

            attrs = el.attrib
            attrsText = ''
            for ak in attrs.keys():
                attrsText += ak + ': ' + str(attrs[ak]) + '; '
            ins = '<p style="' + attrsText + '">' + text + '</p>'
            self.textEdit.insertHtml(ins)
