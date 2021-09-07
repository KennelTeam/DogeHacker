from PyQt5.QtWidgets import *
from Base.UIManager import UIManager
from common.singleton import singleton

@singleton
class MainController:
    ui_manager: UIManager
    main_window: QMainWindow

    def __init__(self):
        self.ui_manager = UIManager()
        self.main_window = self.ui_manager.main_window

