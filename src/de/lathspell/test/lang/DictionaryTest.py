import unittest

class DictionaryTest(unittest.TestCase):
    '''Dictionarys sind Hashmaps'''
    
    def testCreate(self):
        d = {'a': 1, 'b': 2, 'c': 3}

        self.assertTrue(isinstance(d, dict))
        self.assertEqual(3, len(d))
        self.assertEqual(2, d['b'])

        d['d'] = 4
        self.assertEqual(4, len(d))

    def testComplex(self):
        map = { 'roman': ['I', 'II', 'III'],
                'arabic': [1, 2, 3]}
        self.assertEqual('III', map['roman'][2])

    def testAsBoolean(self):
        d = {'a': 1}
        del d['a']
        self.assertEqual(0, len(d))
        self.assertFalse(d)
        self.assertTrue({None: None})

    def testDictionaryComprehension(self):
        a = list(range(65, 68))
        d = {i:chr(i) for i in a}
        self.assertEqual('A', d[65])
        self.assertEqual([65,66,67], list(d.keys()))
        self.assertEqual(['A', 'B', 'C'], list(d.values()))

        # reversing key,value
        d = {v:k for k,v in list(d.items())}
        self.assertEqual({'A':65, 'B':66, 'C':67}, d)
