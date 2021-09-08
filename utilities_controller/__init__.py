import os, sys
import threading
import shutil, ntpath

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../ExternalUtilities')))

existingUtilities = os.listdir('./ExternalUtilities/')


def new_thread_utility(utility):
    utility.run()


def import_utility(utName: str, newThread = False, **kwargs):
    if utName + '.py' not in existingUtilities:
        return 'Utility you request doesn\'t exist'
    
    utImp = __import__(utName)
    instance = utImp.Utility(name = utName, **kwargs)
    if not newThread: 
        return instance
    else:
        p = threading.Thread(target=new_thread_utility, args=(instance,))
        p.start()
        return instance

def install_utility(path: str) -> str:
    try:
        inpFile = 'test_new_util_x01'
        shutil.copy(path, './ExternalUtilities/' + inpFile + '.py')
        import_utility(inpFile)
        shutil.copy( './ExternalUtilities/' + inpFile + '.py', './ExternalUtilities/' + ntpath.basename(path))
        os.remove(path)
        os.remove('./ExternalUtilities/' + inpFile + '.py')
        return 'Installation succeeded'
    except:
        return 'Bad installation'

print(install_utility("C:/Users/alexe/Downloads/snake_game.py"))