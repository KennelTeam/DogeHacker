from EventSystem.event_listener import EventListener
from EventSystem.event import Event
import keyboard
from xml.etree import ElementTree as ET
from PyQt5.QtCore import Qt

class Utility(EventListener):

    def __init__(self, subscription_prefix: str, name: str):
        super().__init__(subscription_prefix)
        self.name = name

    def run(self):
        self.subscribe("keyEvent")
        self.show_text = ">>> "
        self.input_text = ""
        self.update()


    def on_event(self, event: Event):
        print("event")
        if keyboard.is_pressed('enter'):
            print("enter")
            self.show_text += '\n' + self.show_text, "\n>>> "
            self.input_text = ""
            self.update()
        self.update()

    def update(self):
        data = ET.Element("text")
        ET.SubElement(data, "sub_text", color="white").text = self.show_text
        Event(data, self.subscription_prefix + ':on_change:' + self.name)