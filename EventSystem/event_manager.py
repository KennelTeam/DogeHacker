import EventSystem.event
from common.singleton import singleton
import threading


@singleton
class EventManager:
    subscribers: dict = {}
    subscribers_mutex = threading.Lock()

    def subscribe(self, event_type, subscriber):
        # assert isinstance(subscriber, EventSystem.event_listener.EventListener)

        self.subscribers_mutex.acquire()
        if event_type in self.subscribers.keys():
            self.subscribers[event_type].add(subscriber)
        else:
            self.subscribers[event_type] = {subscriber}
        self.subscribers_mutex.release()

    def unsubscribe(self, event_type, subscriber):
        # assert isinstance(subscriber, EventSystem.event_listener.EventListener)
        self.subscribers_mutex.acquire()
        if event_type in self.subscribers.keys():
            if subscriber in self.subscribers[event_type]:
                self.subscribers[event_type].remove(subscriber)
        self.subscribers_mutex.release()

    def register_event(self, event):
        self.subscribers_mutex.acquire()
        # (event.event_type, event.data)
        # (self.subscribers)
        if event.event_type in self.subscribers.keys():
            for subscriber in self.subscribers[event.event_type]:
                process = threading.Thread(target=subscriber.on_event, args=(event, ))
                process.start()
        self.subscribers_mutex.release()
