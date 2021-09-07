from EventSystem.event import Event
from EventSystem.event_manager import EventManager


class EventListener:
    class SubscriptionType:
        ALL = ""

    subscription_prefix = ""

    def real_prefix(self):
        prefix = self.subscription_prefix + ":"
        if self.subscription_prefix == "":
            prefix = ""
        return prefix

    def subscribe(self, event_type: str):
        EventManager.subscribe(self.real_prefix() + event_type, self)

    def unsubscribe(self, event_type: str):
        EventManager.unsubscribe(self.real_prefix() + event_type, self)

    def __init__(self, subscription_prefix=""):
        self.subscription_prefix = subscription_prefix

    # Be careful with multithreading!
    def on_event(self, event: Event):
        pass
