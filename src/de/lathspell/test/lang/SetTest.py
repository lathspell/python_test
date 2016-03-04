import unittest

class SetTest(unittest.TestCase):
    '''Sets sind mutable, unordered, sorted, unique'''
    
    def testCreate(self):
        a = {1, 2}
        self.assertTrue(isinstance(a, set))

        b = {2, 3}
        self.assertEqual({2}, a.intersection(b))
        
        b.add(3)
        self.assertEqual({2,3}, b)

        b.add(4)
        self.assertEqual({2,3,4}, b)

        b.update({5,1})
        self.assertEqual({1,2,3,4,5}, b)

    def testRemove(self):
        a = {1, 2, 3, 4}

        a.discard(666)  # stillschweigend! remove() würde Exception werfen!
        self.assertEqual({1,2,3,4}, a)

        a.remove(2)
        self.assertEqual({1,3,4}, a)

    def testCompare(self):
        a = {1,2,3}
        b = {3,4,5}

        self.assertEqual({1,2,3,4,5}, a.union(b))
        self.assertEqual({3}, a.intersection(b))
        self.assertEqual({1,2}, a.difference(b))
        self.assertEqual({1,2,4,5}, a.symmetric_difference(b))

    def testAsBoolean(self):
        self.assertFalse({})
        self.assertTrue({False})

    def testSetComprehension(self):
        a = {1,2,3,4}
        b = {i for i in a if i % 2 == 0}
        self.assertEqual({2,4}, b)

