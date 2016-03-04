import unittest
from threading import Thread
import time

class AsyncFoo(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.x = 0
    
    def run(self):
        time.sleep(1)
        self.x = 1

class MultiThreadingTest(unittest.TestCase):

    def testMultiThreading(self):
        background = AsyncFoo()
        self.assertEqual(0, background.x)
        background.start()  # The main program continues to run in foreground.
        background.join()   # Wait for the background task to finish
        self.assertEqual(1, background.x)

if __name__ == '__main__':
    unittest.main()

