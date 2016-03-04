import unittest
import logging

class LoggingTest(unittest.TestCase):

    def testLoggin(self):
        # logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        logging.info('Informational message')
        logging.warning('A %s warning!', 'foo')
        
if __name__ == '__main__':
    unittest.main()

