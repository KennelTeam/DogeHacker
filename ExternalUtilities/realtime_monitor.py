from EventSystem.event_listener import EventListener
from EventSystem.event import Event
import requests
import time
import xml.etree.ElementTree as ET

class Utility(EventListener):
    region: str

    def __init__(self, name: str, sub_pref: str, def_region = 'Europe/Moscow'):
        super().__init__(sub_pref)
        self.myname = name
        self.subscribe('ch_city')
        self.region = def_region
        self.site = 'https://worldtimeapi.org/api/timezone/'

    def on_event(self, event: Event):
        self.region = str(event.data)

    def run(self):
        while True:         
            time.sleep(0.1)   
            resp = requests.get(self.site + self.region).json()
            serverTime = resp['datetime'][11:19]            

            rootXML = ET.Element('root')
            textEl = ET.SubElement(rootXML, 'text')
            ET.SubElement(textEl, 'sub_text').text = self.region + ' time is ' + serverTime
            Event(rootXML, self.subscription_prefix + ':onChange:' + self.myname)