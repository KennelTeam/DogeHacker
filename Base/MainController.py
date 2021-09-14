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
        self.subscribe("keyEvent")
        self.main_window = self.ui_manager.main_window
        self.windows = {}
        for id, layout in enumerate(UIManager.main_window.subwindows):
            window_id = "win" + str(id)
            self.windows[window_id] = Window(layout, window_id)
        renderer = Renderer()
        UIManager.app.exec_()

    def on_event(self, event: Event):
        print(event.data)
        event_type = event.event_type.split(":")
        if event_type[0] == "keyEvent":
            for win in self.windows.keys():
                Event(event.data, win + ":" + event_type[0])
        if len(event_type) > 1:
            if event_type[1] == "add_util":
                self.windows[event_type[0]].add_utility(event.data)
