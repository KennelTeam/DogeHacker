from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import sys
import EventSystem.event_listener
from common.singleton import singleton
from EventSystem.event import Event
from CommandsProcessor import parse_command, choose_cmd_action


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)


class CommandLineEdit(QLineEdit):
    def __init__(self, wg):
        self.wg = wg
        super().__init__(wg)

    def keyPressEvent(self, e):
        # if e.key() == QtCore.Qt.Key.Key_Return:
        Event(e.key(), "keyEvent")
        super().keyPressEvent(e)


@singleton
class UIManager(EventSystem.event_listener.EventListener):
    app: QApplication
    form = None
    main_window: MainWindow
    command_line: CommandLineEdit
    window_gridlayout: QGridLayout
    subwindow_layouts: list

    def __init__(self):
        super().__init__()
        self.subscribe("keyEvent")
        self.app = QApplication(sys.argv)
        form_, main_window_ = uic.loadUiType("Base\\MainDesign.ui")
        self.main_window = main_window_()
        self.form = form_()
        self.form.setupUi(self.main_window)
        self.window_gridlayout = self.main_window.findChild(QGridLayout, "mainWindowsLayout")
        self.subwindow_layouts = self.main_window.findChildren(QFormLayout)

        self.setup_ui()
        self.main_window.show()

    def setup_ui(self):
        command_line = self.main_window.findChild(QLineEdit, "commandLine")
        command_line.hide()
        self.command_line = CommandLineEdit(self.main_window)
        central_widget = self.main_window.findChild(QWidget, "centralwidget")
        self.command_line.setParent(central_widget)
        self.command_line.move(command_line.x(), command_line.y())
        self.command_line.resize(command_line.size())

    def on_event(self, event: Event):
        print("on_event")
        if event.data == QtCore.Qt.Key.Key_Return:
            params = parse_command(self.command_line.text())
            choose_cmd_action(params)
