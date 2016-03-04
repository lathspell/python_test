import unittest
from decimal import *

class DecimalsTest(unittest.TestCase):

    def testDecimals(self):
        x = Decimal('0.70') * Decimal('1.05')
        self.assertEqual(Decimal('0.7350'), x)
        self.assertEqual(Decimal('0.74'), x.quantize(Decimal('0.01')))  # round to nearest cent
        self.assertEqual(0.73, round(.70 * 1.05, 2)) # python3.2 only!

if __name__ == '__main__':
    unittest.main()

