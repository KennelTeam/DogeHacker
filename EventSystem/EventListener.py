from EventSystem.Event import Event
from EventSystem.EventManager import EventManager


class EventListener:
    __subscription_prefix = ""

    def subscribe(self, event_type: str):
        EventManager.subscribe(self.__subscription_prefix + event_type, self)

    def __init__(self, subscription_prefix=""):
        self.__subscription_prefix = subscription_prefix

    def on_event(self, event: Event):
        pass
