import time

from EventSystem.event_listener import EventListener
from EventSystem.event import Event
from xml.etree import ElementTree


class HackPentagonUtility(EventListener):
    hacking_time = 10
    progress_bar_size = 10
    name: str

    def __init__(self, prefix: str, name: str):
        super(HackPentagonUtility, self).__init__(prefix)
        self.name = name

    def run(self):
        print("test")
        for i in range(self.progress_bar_size):
            et = self.prepare_element(i)
            Event(et, self.subscription_prefix + ":on_change:" + self.name)
            time.sleep(self.hacking_time / self.progress_bar_size)

        et = self.prepare_element(self.progress_bar_size)
        status = ElementTree.SubElement(et, "text", color="green")
        status.text = "Access Granted"

        data = ElementTree.SubElement(et, "text", color="red")
        data.text = "Secure pentagon data: BbI Bce ncbI"

        Event(et, self.subscription_prefix + ":on_change:" + self.name)

    def prepare_element(self, step):
        main = ElementTree.Element("xml")

        if step != self.progress_bar_size:
            title = ElementTree.SubElement(main, "text")
            title.text = "Hacking pentagon in progress." + ("." * (step % 3))
        else:
            title = ElementTree.SubElement(main, "text", color="green")
            title.text = "Hacking pentagon completed."
        progress_bar_text = "|" + "█" * step + " " * (self.progress_bar_size - step) + "|" + \
                            str(round((100.0 * step / self.progress_bar_size) * 10) / 10.0) + "% done"
        progress_bar = ElementTree.SubElement(main, "text")
        progress_bar.text = progress_bar_text

        return main
