import unittest
from EventSystem.event_listener import EventListener
from EventSystem.event import Event
from EventSystem.event_manager import EventManager
import sys
import os


class EventListenerTest(EventListener):
    event_happened = False
    event_type = ""
    event_data = ""

    def on_event(self, event: Event):
        self.event_happened = True
        self.event_type = event.event_type
        self.event_data = event.data


class EventSystemTest(unittest.TestCase):
    def testHappens(self):
        testData = "cringe"

        testListener = EventListenerTest()
        testListener.subscribe("testEvent")

        self.assertEqual(testListener.event_happened, False, "Event is not happened, but event_happened is true")

        _ = Event(testData, "testEvent")

        self.assertEqual(testListener.event_happened, True, "Event is happened, but event_happened is false")
        self.assertEqual(testListener.event_type, "testEvent", "event type is not set")
        self.assertEqual(testListener.event_data, testData, "event data is wrong")

    def testNotHappens(self):
        testData = "cringe"

        testListener = EventListenerTest()
        testListener.subscribe("testEvent")

        self.assertEqual(testListener.event_happened, False, "Event is not happened, but event_happened is true")

        _ = Event(testData, "testEventWrong")

        self.assertEqual(testListener.event_happened, False,
                         "Event with wrong type happened, but event_happened is true")


if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    event_manager = EventManager
    unittest.main()
