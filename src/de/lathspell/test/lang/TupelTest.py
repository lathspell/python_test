import unittest

class TupelTest(unittest.TestCase):
    '''Tupel sind read-only Listen'''

    def testCreate(self):
        a = ('a', 'beh', 1, False, None, 'z')
        self.assertEqual(6, len(a))
        self.assertEqual('a', a[0])
        self.assertEqual(0, a[3]) # casting False
        self.assertEqual('z', a[-1])

        self.assertEqual(('beh', 1), a[1:3]) # slice
        self.assertEqual(('z',), a[5:]) # left inclusive; Komma ist wichtig!
        self.assertEqual(('a',), a[:1]) # right exclusive; Komma ist wichtig!
        self.assertEqual(a, a[:]) # complete list

        b = (1,)
        b = b + (2,)
        self.assertEqual((1,2), b)

        (c1, c2) = b
        self.assertEqual(1, c1)
        self.assertEqual(2, c2)


    def testSearch(self):
        a = (1,4,2,3,4)

        self.assertEqual(2, a.count(4))
        self.assertTrue(3 in a)
        self.assertEqual(2, a.index(2))
        
    def testListsAsBooleans(self):
        self.assertTrue((False,))
        self.assertFalse(())

    def testConvert(self):
        a = (1,2,3)
        t = tuple(a) # Klassen-Constructor, keine Funktion?
        a2 = list(t)
        self.assertTrue(isinstance(t, tuple)) # Klasse mit Kleinbuchstaben
        self.assertTrue(isinstance(a2, list))

