import unittest
import repr
import pprint


class ReprTestCase(unittest.TestCase):
    def testRepr(self):
        myset = set('supercalifragilisticexpialidocious')
        self.assertEqual("set(['a', 'c', 'e', 'd', 'g', 'f', 'i', 'l', 'o', 'p', 's', 'r', 'u', 't', 'x'])", myset.__str__())
        self.assertEqual("set(['a', 'c', 'd', 'e', 'f', 'g', ...])", repr.repr(myset));
        
    def testPprint(self):
        complx = [1, 'a', {'A': 41}]
        formatted = pprint.pformat(complx, width=10, indent=4);
        self.assertEqual("[   1,\n    'a',\n    {   'A': 41}]", formatted)
    
        
if __name__ == '__main__':
    unittest.main()

