import EventSystem.event
import EventSystem.event_listener
from common.singleton import singleton
import multiprocessing


@singleton
class EventManager:
    subscribers: dict = {}
    subscribers_mutex = multiprocessing.Lock()

    def subscribe(self, event_type, subscriber):
        assert isinstance(subscriber, EventSystem.event_listener.EventListener)

        with self.subscribers_mutex:
            if event_type in self.subscribers.keys():
                self.subscribers[event_type].append(subscriber)
            else:
                self.subscribers[event_type] = [subscriber]
            self.subscribers_mutex.release()

    def register_event(self, event):
        with self.subscribers_mutex:
            if event.event_type in self.subscribers.keys():
                for subscriber in self.subscribers[event.event_type]:
                    process = multiprocessing.Process(target=subscriber.on_event, args=(subscriber, event, ))
                    process.start()
