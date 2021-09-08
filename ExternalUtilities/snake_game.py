from EventSystem.event_listener import EventListener
from EventSystem.event import Event
import time
import random

import xml.etree.ElementTree as ET

class Utility(EventListener):
    x: int
    y: int
    width: int
    height: int
    tail: list
    xdir = 0
    ydir = 1
    xApple: int
    yApple: int

    def __init__(self, name: str, sub_pref: str, width: int, height: int):
        super().__init__(sub_pref)
        self.x = width // 2
        self.y = height // 2
        self.width = width
        self.height = height
        self.tail = []
        
    def on_event(self, event: Event):
        key = event.data
        if key == 'd':
            if self.ydir == -1:
                self.xdir = 1
                self.ydir = 0
            elif self.ydir == 1:
                self.xdir = -1
                self.ydir = 0
            elif self.xdir == 1:
                self.ydir = 1
                self.xdir = 0
            elif self.xdir == -1:
                self.ydir = -1
                self.xdir = 0
        
        elif key == 'a':
            if self.ydir == -1:
                self.xdir = -1
                self.ydir = 0
            if self.ydir == 1:
                self.ydir = 1
                self.ydir = 0
            elif self.xdir == 1:
                self.ydir = -1
                self.xdir = 0
            elif self.xdir == -1:
                self.ydir = 1
                self.xdir = 0


    def newAppleCord(self):
        self.xApple = random.randint(0, self.width-1)
        self.yApple = random.randint(0, self.height-1)

    def run(self):
        while True:
            time.sleep(1)
            self.tail.append((self.x, self.y))
            self.x += self.xdir
            self.y += self.ydir
            if self.x == self.xApple and self.y == self.yApple:
                self.newAppleCord()
            else:
                self.tail.pop()

            numsField = []
            for i in range(self.width+2):
                numsField.append([])
                for a in range(self.height+2):
                    numsField.append(0)
            
            for i in range(self.width+2):
                numsField[0][i] = 1
                numsField[-1][i] = 1
                numsField[i][0] = 1
                numsField[i][-1] = 1

            for tel in self.tail:
                numsField[tel[0]][tel[1]] = 2
            
            numsField[self.x][self.y] = 3
            numsField[self.xApple][self.yApple] = 4

            sField = ''

            for row in numsField:
                for el in row:
                    if el == 0:
                        sField += ' '
                    elif el == 1:
                        sField += '#'
                    elif el == 2:
                        sField += '*'
                    elif el == 3:
                        sField += '@'
                    elif el == 4:
                        sField += '^'
                sField += '\n'

            rootXML = ET.Element('root')
            textEl = ET.SubElement(rootXML, 'text')
            ET.SubElement(textEl, 'sub_text').text = sField
            Event(rootXML, self.subscription_prefix + ':onChange:' + self.myname)