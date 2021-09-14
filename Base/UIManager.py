from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
import sys
import EventSystem.event_listener
from common.singleton import singleton
from EventSystem.event import Event
from CommandsProcessor import parse_command, choose_cmd_action


class CommandLineWidget(QLineEdit):
    def __init__(self, wg):
        self.wg = wg
        super().__init__(wg)

    def keyPressEvent(self, e):
        Event(e.key(), "keyEvent")
        super().keyPressEvent(e)


class MainWindow(QWidget):
    main_grid_layout: QGridLayout
    grid_columns_count = 1
    grid_rows_count = 1
    command_line: QWidget
    subwindows = list()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("DogeHacker")
        self.setStyleSheet("background-color: #303030;"
                           "color: #DDDDDD;")
        self.main_grid_layout = QGridLayout()
        self.main_grid_layout.setSpacing(0)
        self.setLayout(self.main_grid_layout)

        for column in range(self.grid_columns_count):
            for row in range(self.grid_rows_count):
                self.add_subwindow((row, column))

        self.command_line = CommandLineWidget(self)
        self.command_line.setFont(QFont("Courier", 12))
        self.command_line.setContentsMargins(0, 10, 0, 0)
        self.command_line.setFocus()
        self.main_grid_layout.addWidget(self.command_line, self.grid_rows_count, 0, 1, self.grid_columns_count)

    def add_subwindow(self, position: tuple):
        scroll_area = QScrollArea()
        form_layout = QFormLayout()
        form_layout.setContentsMargins(0, 0, 0, 0)
        scroll_area.setLayout(form_layout)
        self.subwindows.append(form_layout)
        self.main_grid_layout.addWidget(scroll_area, position[0], position[1])


@singleton
class UIManager(EventSystem.event_listener.EventListener):
    app: QApplication
    main_window: MainWindow

    def __init__(self):
        super().__init__()
        self.subscribe("keyEvent")
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.main_window.setGeometry(100, 100, 800, 600)
        self.main_window.show()

    def on_event(self, event: Event):
        print("on_event")
        if event.data == QtCore.Qt.Key_Return:
            params = parse_command(self.main_window.command_line.text())
            choose_cmd_action(params)
