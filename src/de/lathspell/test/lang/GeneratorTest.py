import unittest

class GeneratorTest(unittest.TestCase):

    def squares(self, a):
        for i in a:
            yield ((i, i*i) if i % 2 == 0 else None)

    def testGenerator(self):
        x = self.squares([1,2,3])

        # Das x Objekt könnte auch mit for iteriert werden
        self.assertEqual(None, next(x))
        self.assertEqual((2,4), next(x))
        self.assertEqual(None, next(x))


