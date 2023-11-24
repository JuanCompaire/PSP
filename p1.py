import threading
import queue

q = queue.Queue()

class Productor(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        pass

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        pass

p = Productor(q)
c = Consumer(q)

p.start()
c.start()

p.join()
c.join()