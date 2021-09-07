import os, sys
from multiprocessing import Process

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ExternalUtilities')))

existingUtilities = os.listdir('./ExternalUtilities/')

def new_thread_utility(utility):
    utility.run()

def import_utility(utName: str, newThread = False, **kwargs):
    if utName + '.py' not in existingUtilities:
        return 'Utility you request doesn\'t exist'
    
    utImp = __import__(utName)
    instance = utImp.Utility(**kwargs)
    if not newThread: 
        return instance
    else:
        p = Process(target=new_thread_utility, args=(instance,))
        p.start()
        return instance