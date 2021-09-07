from EventSystem.Event import Event
from common.singleton import singleton


@singleton
class EventManager:
    subscribers: dict

    def __init__(self):
        pass

    def subscribe(self, event_type, subscriber):
        if event_type in self.subscribers.keys():
            self.subscribers[event_type].append(subscriber)
        else:
            self.subscribers[event_type] = [subscriber]

    def register_event(self, event: Event):
        pass