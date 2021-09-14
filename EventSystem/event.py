import EventSystem.event_manager
from PyQt5.QtCore import QObject


class Event(QObject):
    event_type: str
    data: any

    def __init__(self):
        super(Event, self).__init__(None)

    @staticmethod
    def emit(data, event_type: str):
        print("EVENT!!!")
        event = Event()
        event.data = data
        event.event_type = event_type
        print("emitting")
        EventSystem.event_manager.EventManager.register_event(event)

    def copy(self):
        new_event = Event()
        new_event.data = self.data
        new_event.event_type = self.event_type
        return new_event
