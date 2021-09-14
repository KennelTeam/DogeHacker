import time

from EventSystem.event_listener import EventListener
from EventSystem.event import Event
from xml.etree import ElementTree
from PyQt5.QtCore import Qt
import threading
import random


class Utility(EventListener):
    points = []
    delta = 0
    deltaD = 0.03
    current = 5
    max_size = 50

    def __init__(self, subscription_prefix: str, name: str):
        super(Utility, self).__init__(subscription_prefix)
        self.name = name
        self.subscribe("stonks")
        self.subscribe("not_stonks")
        self.subscribe("keyEvent")
        self.points = []
        self.delta = 0.5
        self.deltaD = 1.0
        self.stopped = False
        self._mutex = threading.Lock()

    def on_event(self, event: Event):
        print(event.event_type, event.data)
        self._mutex.acquire()
        print("!!!")
        print(event.event_type.split(":")[1])
        print(self.deltaD)
        if event.event_type.split(":")[1] == "stonks":
            self.delta += self.deltaD
        elif event.event_type.split(":")[1] == "not_stonks":
            print("not stonks!!!\n\n")
            self.delta -= self.deltaD
        elif event.data == Qt.Key.Key_C:
            self.stopped = True
        self._mutex.release()

    def run(self):
        while not self.stopped:
            self._mutex.acquire()

            if len(self.points) == self.max_size:
                self.points = self.points[1:]

            self.current += self.delta + (random.random() - 0.5) * 0.03
            self.points.append(self.current)

            xml = self.prepare_xml()
            Event(xml, self.subscription_prefix + ":on_change:" + self.name)
            print(self.delta)
            self._mutex.release()

            time.sleep(1)

        Event(ElementTree.Element("text"), self.subscription_prefix + ":on_change:" + self.name)

    def prepare_xml(self):
        root = ElementTree.Element("graph")
        root.text = ""
        for point in self.points:
            root.text += str(int(point * 10)) + " "
        return root

