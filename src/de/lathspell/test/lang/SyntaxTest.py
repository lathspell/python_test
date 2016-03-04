import unittest

class SyntaxTest(unittest.TestCase):

    def testTernary(self):
        x = True if (1 < 2) else False
        self.assertTrue(x)

    def testRangedCondition(self):
        n = 15
        self.assertTrue(10 < n < 20)


