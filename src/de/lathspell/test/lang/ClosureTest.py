import unittest

class  ClosureTestCase(unittest.TestCase):

    def doMinus(self, a, b):
        return a-b

    def testClosure(self):
        x = self.calc(6, '-', 4)
        self.assertEqual(2, x)

    def calc(self, a, sign, b):
        patterns = \
            {
                '-': self.doMinus,
                '+': 'TODO self.doPlus',
                '/': 'TODO self.doDivide',
                '*': 'TODO self.doMultiply',
            }
        return patterns[sign](a, b)

