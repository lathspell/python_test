from fractions import Fraction
import unittest
import math

class DataTypesTest(unittest.TestCase):
    #def setUp(self):
    #    self.foo = DataTypes()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def testNull(self):
        null1=None;
        self.assertEqual(None, null1)

    def testBool(self):
        bool1 = False
        self.assertFalse(bool1)
        bool2 = not bool1
        self.assertTrue(bool2)

    def testNumeric(self):
        int1 = 42
        self.assertEqual(42, int1)
        self.assertTrue(isinstance(int1, int))
        float1 = 3.14
        self.assertEqual(3.14, float1)
        self.assertTrue(isinstance(float1, float))

    def testOperators(self):
        self.assertEqual(5.5, 11/2) # normal devision
        self.assertEqual(5, 11//2) # truncating devision
        self.assertEqual(1, 11 % 2) # modulo
        self.assertEqual(8, 2**3)

    def testFractions(self):
        f1 = Fraction(6/9)
        self.assertEqual(2/3, f1)
        f2 = Fraction(2/3)
        f3 = f1 + f2
        self.assertEqual(Fraction(4/3), f3)
        self.assertEqual(4/3, f3)

    def testTrigonometry(self):
        self.assertEqual(1, math.sin(math.pi / 2))

    def testBooleansAsNumbers(self):
        self.assertEqual(0, 1*False)
        self.assertEqual(1, 1*True)
        self.assertEqual(2, 2*True)