from multiprocessing import Queue
import time

class Utility:
    def __init__(self, queue: Queue):
        time.sleep(3000)
        queue.put('Hi buddy')