from ExternalUtilities.hack_pentagon import HackPentagonUtility
from xml.etree import ElementTree
from EventSystem.event import Event
from EventSystem.event_listener import EventListener
from EventSystem.event_manager import EventManager


class TestHackPentagon(EventListener):
    def __init__(self):
        super().__init__()
        self.subscribe(":on_change:test")

    def on_event(self, event: Event):
        print("on_change")
        ElementTree.dump(event.data)


event_manager = EventManager
thp = TestHackPentagon()
hpu = HackPentagonUtility("", "test")
hpu.run()
