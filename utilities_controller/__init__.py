import os, sys
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ExternalUtilities')))

existingUtilities = os.listdir('./ExternalUtilities/')


def new_thread_utility(utility):
    utility.run()


def import_utility(utName: str, newThread = False, **kwargs):
    if utName + '.py' not in existingUtilities:
        return 'Utility you request doesn\'t exist'
    
    utImp = __import__(utName)
    instance = utImp.Utility(name=utName, **kwargs)
    if not newThread: 
        return instance
    else:
        p = threading.Thread(target=new_thread_utility, args=(instance,))
        p.start()
        return instance