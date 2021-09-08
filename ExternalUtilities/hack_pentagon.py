import time

from EventSystem.event_listener import EventListener
from EventSystem.event import Event
from xml.etree import ElementTree


class Utility(EventListener):
    hacking_time = 10
    progress_bar_size = 10
    name: str

    def __init__(self, subscription_prefix: str, name: str):
        super(Utility, self).__init__(subscription_prefix)
        self.name = name

    def run(self):
        for i in range(self.progress_bar_size):
            et = self.prepare_element(i)
            Event(et, self.subscription_prefix + ":on_change:" + self.name)
            time.sleep(self.hacking_time / self.progress_bar_size)

        et = self.prepare_element(self.progress_bar_size)
        status = ElementTree.SubElement(et, "sub_text", color="green")
        status.text = "Access Granted"

        data = ElementTree.SubElement(et, "sub_text", color="red")
        data.text = "Secure pentagon data: BbI Bce ncbI"

        Event(et, self.subscription_prefix + ":on_change:" + self.name)

    def prepare_element(self, step):
        main = ElementTree.Element("text")

        if step != self.progress_bar_size:
            title = ElementTree.SubElement(main, "sub_text")
            title.text = "Hacking pentagon in progress." + ("." * (step % 3))
        else:
            title = ElementTree.SubElement(main, "sub_text", color="green")
            title.text = "Hacking pentagon completed."
        progress_bar_text = "|" + "█" * step + " " * (self.progress_bar_size - step) + "|" + \
                            str(round((100.0 * step / self.progress_bar_size) * 10) / 10.0) + "% done"
        progress_bar = ElementTree.SubElement(main, "sub_text")
        progress_bar.text = progress_bar_text

        return main
