import unittest

class ListTest(unittest.TestCase):
    
    def testCreate(self):
        a = ['a', 'beh', 1, False, None, 'z']
        self.assertEqual(6, len(a))
        self.assertEqual('a', a[0])
        self.assertEqual(0, a[3]) # casting False
        self.assertEqual('z', a[-1])

        self.assertEqual(['beh', 1], a[1:3]) # slice
        self.assertEqual(['z'], a[5:]) # left inclusive
        self.assertEqual(['a'], a[:1]) # right exclusive
        self.assertEqual(a, a[:]) # complete list

        b = [1]
        b = b + [2]
        self.assertEqual([1,2], b)
        b.append(3)
        self.assertEqual([1,2,3], b)
        b.extend([4,5])
        self.assertEqual([1,2,3,4,5], b)
        b.insert(5, 7)
        self.assertEqual([1,2,3,4,5,7], b)
        b.insert(-1, 6)
        self.assertEqual([1,2,3,4,5,6,7], b)

    def testSearch(self):
        a = [1,4,2,3,4]

        self.assertEqual(2, a.count(4))
        self.assertTrue(3 in a)
        self.assertEqual(2, a.index(2))

    def testRemove(self):
        a = [1, 2, 3, 4]

        a.remove(3)
        self.assertEqual([1,2,4], a)
        popped = a.pop(2)
        self.assertEqual(4, popped)
        self.assertEqual([1,2], a)
        popped = a.pop()
        self.assertEqual(2, popped)
        self.assertEqual([1], a)
        del a[0]
        self.assertEqual([], a) # leere Liste

    def testMisc(self):
        a = [1,2,3]

        a.reverse()
        self.assertEqual([3,2,1], a)

    def testListsAsBooleans(self):
        self.assertTrue([False])
        self.assertFalse([])

    def testListComprehension(self):
        a = [1, 9, 8, 4]
        b = [i*2 for i in a]
        self.assertEqual([2, 18, 16, 8], b)

        # Es wird über alle Elemente i in der Liste a iteriert
        # und genau dann i zurück geliefert, wenn i gerade ist
        c = [i for i in a if i % 2 == 0]
        self.assertEqual([8,4], c)

    def testRanges(self):
        a = list(range(0, 3))
        self.assertEqual([0,1,2], list(a))

    def testZip(self):
        a = [1,2,3]
        b = ['A', 'B', 'C']
        zipped_obj = list(zip(a, b))
        zipped = list(zipped_obj)
        self.assertEqual((2, 'B'), zipped[1])
        self.assertEqual((3, 'C'), zipped[2])

        aa, bb = list(zip(*zipped))
        self.assertEqual(tuple(a), aa)
        self.assertEqual(tuple(b), bb)
