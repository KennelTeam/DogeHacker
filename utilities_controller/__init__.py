import os, sys
from multiprocessing import Process, Queue

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ExternalUtilities')))

existingUtilities = os.listdir('./ExternalUtilities/')

class Proc(Process):
    def __init__(self, utilityClass, queue, kwargs):
        super(Proc, self).__init__()
        self.kwargs = kwargs
        self.utClass = utilityClass
        self.queue = queue
    
    def run(self):
        self.utClass(self.queue, **self.kwargs)



def import_utility(utName: str, newThread = True, **kwargs):
    if utName + '.py' not in existingUtilities:
        return 'Utility you request doesn\'t exist'
    
    utImp = __import__(utName)
    if not newThread: 
        instance = utImp.Utility(**kwargs)
        return instance
    else:
        queue = Queue()
        proc = Proc(utImp.Utility, queue, kwargs)
        return proc