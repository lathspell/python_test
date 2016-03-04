# coding: utf-8
import unittest

class DataTypesTestCase(unittest.TestCase):
    def multiply(a,b,xfactor=1):
        '''
        Multipliziert zwei Zahlen.

        @param float a
        @param float b
        @return float
        '''
        return a*b*xfactor;

        def testIt():
            self.assertEquals(3,4)
            
if __name__ == '__main__':
    unittest.main()
#    print multiply(3,4)
#    unittest.assertEqual(x, y, "Msg");
#    print multiply(3,4, xfactor=9)
