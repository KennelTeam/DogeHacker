import EventSystem.event
from common.singleton import singleton
from common.thread import HackerThread, HackerMutex
from functools import partial


@singleton
class EventManager:
    subscribers: dict = {}
    subscribers_mutex = HackerMutex()

    def subscribe(self, event_type, subscriber):
        # assert isinstance(subscriber, EventSystem.event_listener.EventListener)

        self.subscribers_mutex.lock()
        if event_type in self.subscribers.keys():
            self.subscribers[event_type].add(subscriber)
        else:
            self.subscribers[event_type] = {subscriber}
        self.subscribers_mutex.unlock()

    def unsubscribe(self, event_type, subscriber):
        # assert isinstance(subscriber, EventSystem.event_listener.EventListener)
        self.subscribers_mutex.lock()
        if event_type in self.subscribers.keys():
            if subscriber in self.subscribers[event_type]:
                self.subscribers[event_type].remove(subscriber)
        self.subscribers_mutex.unlock()

    def register_event(self, event):
        print("THERE!!!")
        self.subscribers_mutex.lock()
        print(event.event_type, event.data)
        print(self.subscribers)
        if event.event_type in self.subscribers.keys():
            print("subscribers: ", self.subscribers[event.event_type])
            for subscriber in self.subscribers[event.event_type]:
                print("s: ", subscriber)
                event_copy = event.copy()
                func = partial(subscriber.on_event, event_copy)
                runner = HackerThread(func)
                runner.run()
        else:
            print("NO SUBSCRIBERS\n")
        print("unlocking")
        self.subscribers_mutex.unlock()
