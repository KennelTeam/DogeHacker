import EventSystem.Event
import EventSystem.EventListener
from common.singleton import singleton


@singleton
class EventManager:
    subscribers: dict = {}

    def subscribe(self, event_type, subscriber):
        assert isinstance(subscriber, EventSystem.EventListener.EventListener)

        if event_type in self.subscribers.keys():
            self.subscribers[event_type].append(subscriber)
        else:
            self.subscribers[event_type] = [subscriber]

    def register_event(self, event):
        if event.event_type in self.subscribers.keys():
            for subscriber in self.subscribers[event.event_type]:
                subscriber.on_event(event)
