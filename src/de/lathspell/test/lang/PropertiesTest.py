import unittest

class PropertiesTest(unittest.TestCase):
    class SubClass1(object):
        ''' This is a subclass'''
        
        def __init__(self):
            self.a = 1
            self._b = 2
            
        @property
        def b(self):
            return self._b

        @b.setter
        def b(self, value):
            self._b = 2 * value;

    def testProperties(self):
        sub = PropertiesTest.SubClass1()
        self.assertEqual(1, sub.a)
        self.assertEqual(2, sub.b)

        # normal set
        sub.a = 11
        self.assertEqual(11, sub.a)

        # value changed by property method
        sub.b = 22
        self.assertEqual(44, sub.b)
        