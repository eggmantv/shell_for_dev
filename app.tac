"""
Usage:

$ pip install -r requirements.txt
$ twistd -noy worker.tac
"""

from twisted.application import service, internet

class App(object):
    counter = 0

    def worker(self):
        self.counter += 1
        print(self.counter)

    def getService(self):
        return internet.TimerService(1, self.worker)

application = service.Application("worker")
service = App().getService()
service.setServiceParent(application)
