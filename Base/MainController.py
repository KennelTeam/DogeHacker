import sys
import threading
import time

from PyQt5.QtWidgets import *
from Base.UIManager import UIManager
from EventSystem.event import Event
from common.singleton import singleton
from Windows.window import Window
from EventSystem.event_listener import EventListener
from Renderer import Renderer


@singleton
class MainController(EventListener):
    ui_manager: UIManager
    main_window: QMainWindow
    windows: {}

    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager
        print("there")
        self.main_window = self.ui_manager.main_window
        print("starting windows")
        self.windows = {}
        for id, layout in enumerate(UIManager.subwindow_layouts):
            window_id = "win" + str(id)
            self.windows[window_id] = Window(layout, window_id)
        print(self.windows)
        renderer = Renderer()
        UIManager.app.exec_()

    def on_event(self, event: Event):
        event_type = event.event_type.split(":")
        if len(event_type) > 1:
            if event_type[1] == "add_util":
                self.windows[event_type[0]].add_utility(event.data)
