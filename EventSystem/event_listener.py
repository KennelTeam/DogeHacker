from EventSystem.event import Event
from EventSystem.event_manager import EventManager


class EventListener:
    class SubscriptionType:
        ALL = ""

    __subscription_prefix = ""

    def subscribe(self, event_type: str):
        EventManager.subscribe(self.__subscription_prefix + ":" + event_type, self)

    def unsubscribe(self, event_type: str):
        EventManager.unsubscribe(self.__subscription_prefix + ":" + event_type, self)

    def __init__(self, subscription_prefix=""):
        self.__subscription_prefix = subscription_prefix

    # Be careful with multithreading!
    def on_event(self, event: Event):
        pass
