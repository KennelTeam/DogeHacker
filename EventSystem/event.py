import EventSystem.event_manager


class Event:
    event_type: str
    data: any

    def __init__(self, data, event_type: str):
        self.data = data
        self.event_type = event_type
        EventSystem.event_manager.EventManager.register_event(self)

