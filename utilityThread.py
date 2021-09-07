from multiprocessing import Queue
import time

class Utility:
    def __init__(self, queue: Queue):
        queue.put('Hi buddy')