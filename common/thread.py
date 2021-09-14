from PyQt5.QtCore import QObject, QMutex, QThread, QRunnable
import threading


class HackerThread(QRunnable):
    def __init__(self, function_to_run):
        super(HackerThread, self).__init__(None)
        self.function = function_to_run

    def run(self):
        thread = threading.Thread(target=self.function)
        thread.start()


class HackerMutex:
    def __init__(self):
        self._mutex = threading.Lock()

    def lock(self):
        self._mutex.acquire()

    def unlock(self):
        self._mutex.release()