import PyQt5.QtWidgets

from EventSystem.event import Event
from EventSystem.event_manager import EventManager
from EventSystem.event_listener import EventListener
from utilities_controller import import_utility
import threading
from Renderer import Renderer, render
from xml.etree import ElementTree


class Window(EventListener):
    layout: PyQt5.QtWidgets.QFormLayout
    window_id: str
    root_utilities: dict
    utilities_xmls: dict
    utilities_mutex: threading.Lock

    def __init__(self, layout: PyQt5.QtWidgets.QFormLayout, window_id: str):
        super(Window, self).__init__(window_id)
        self.utilities_xmls = {}
        self.layout = layout
        self.window_id = window_id
        self.subscribe(EventListener.SubscriptionType.ALL)
        self.subscribe("add_util")
        self.root_utilities = {}
        self.utilities_mutex = threading.Lock()

    def on_event(self, event: Event):
        print("Window on_event is called")
        event_type = event.event_type.split(self.window_id)[1].split(":")[1:]
        print(event_type)
        if event_type[0] == 'on_change':
            self.utilities_mutex.acquire()
            print("on_change called")
            if event_type[1] in self.root_utilities.keys():
                self.utilities_xmls[event_type[1]] = event.data
                print("starting redrawing")
                redrawing = threading.Thread(target=self.redraw, args=())
                redrawing.start()
            self.utilities_mutex.release()
        elif event_type[0] == 'on_error':
            self.utilities_mutex.acquire()
            if event_type[1] in self.root_utilities.keys():
                # Process errors here
                pass
            self.utilities_mutex.release()
        elif event_type[0] == "add_util":
            print("adding utility")
            self.add_utility(event.data)

    def redraw(self):
        print("redraw")
        result_xml = ElementTree.Element("xml")
        for utility in self.utilities_xmls.keys():
            xml = self.utilities_xmls[utility]
            result_xml.append(xml)
        print("RENDER!!!")
        ElementTree.dump(result_xml)
        Renderer.instance.render.emit(self.layout, result_xml)
        # render(self.layout, result_xml)

    def add_utility(self, utility_name):
        self.utilities_mutex.acquire()
        print("add_utility is called")
        print(self.real_prefix() + utility_name + ":on_change")
        self.subscribe("on_change:" + utility_name)
        self.subscribe("on_error:" + utility_name)
        self.root_utilities[utility_name] = import_utility(utility_name, True, subscription_prefix=self.window_id)
        self.utilities_xmls[utility_name] = ""
        self.utilities_mutex.release()

    def remove_utility(self, utility_name):
        self.utilities_mutex.acquire()
        self.unsubscribe(utility_name)
        self.root_utilities[utility_name].terminate()
        self.utilities_xmls.pop(utility_name)
        self.utilities_mutex.release()
