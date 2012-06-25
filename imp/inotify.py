"""
this script watches the changes under this directory and
auto restart main.py
"""
import os, sys, time
import pyinotify
import subprocess
from pyinotify import WatchManager, Notifier, ThreadedNotifier, EventsCodes, ProcessEvent

class PTmp(ProcessEvent):
    def __init__(self):
        self.p = subprocess.Popen('python main.py', shell=True)
        
    def process_IN_MODIFY(self, event):
        if self.p.poll() == None:
            self.p.kill()
        print "Modify: %s, restarting main.py" %  \
                os.path.join(event.path, event.name)
        self.p = subprocess.Popen('python main.py', shell=True)

        
def watcher():
    wm = WatchManager()
    mask = pyinotify.IN_MODIFY|pyinotify.IN_CREATE|pyinotify.IN_DELETE # the watch event 
    ptmp = PTmp()
    
    notifier = ThreadedNotifier(wm, ptmp)
    notifier.start()
    wdd = wm.add_watch('.', mask, rec=True)

    while True:
        x = 0
        try:
            x = 1
            time.sleep(.3)
        except KeyboardInterrupt:
            wm.rm_watch(wdd.values())
            ptmp.p.kill()
            notifier.stop()
            sys.exit(0)



if __name__ == '__main__':
    watcher()
