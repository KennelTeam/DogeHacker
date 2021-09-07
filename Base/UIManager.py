from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import sys
import EventSystem.event_listener
from common.singleton import singleton
from EventSystem.event import Event
from CommandsProcessor import parse_command


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


class CommandLineEdit(QLineEdit):
    def __init__(self, wg):
        self.wg = wg
        super().__init__(wg)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key.Key_Return:
            Event(e.key(), "keyEvent")
        super().keyPressEvent(e)


@singleton
class UIManager(EventSystem.event_listener.EventListener):
    __app: QApplication
    form = None
    main_window: MainWindow
    command_line: CommandLineEdit
    window_gridlayout: QGridLayout
    subwindow_layouts: list

    def __init__(self):
        super().__init__()
        self.subscribe("keyEvent")
        self.__app = QApplication(sys.argv)
        form_, main_window_ = uic.loadUiType("Base\\MainDesign.ui")
        self.main_window = main_window_()
        self.form = form_()
        self.form.setupUi(self.main_window)
        self.window_gridlayout = self.main_window.findChild(QGridLayout, "mainWindowsLayout")
        self.subwindow_layouts = self.window_gridlayout.children()
        self.setup_ui()
        self.main_window.show()
        sys.exit(self.__app.exec_())

    def setup_ui(self):
        command_line = self.main_window.findChild(QLineEdit, "commandLine")
        command_line.hide()
        self.command_line = CommandLineEdit(self.main_window)
        central_widget = self.main_window.findChild(QWidget, "centralwidget")
        self.command_line.setParent(central_widget)
        self.command_line.move(command_line.x(), command_line.y())
        self.command_line.resize(command_line.size())

    def on_event(self, event: Event):
        # print(self.command_line.text())
        parse_command(self.command_line.text())

