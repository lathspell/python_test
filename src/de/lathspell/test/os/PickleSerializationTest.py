import os.path
import os
import unittest
import pickle

class PickleSerializationTest(unittest.TestCase):
    """
    cpickle ist eine Altlast von Python2, in Python3 kann man einfach nur
    "import pickle" schreiben.
    """
    
    def setUp(self):
        if (os.path.isfile('pickle.tmp')):
            os.unlink('pickle.tmp')

    def tearDown(self):
        self.setUp()

    def testSerialization(self):
        data = {
            'first_name': 'Max',
            'last_name': 'Mustermann',
            'bday': '1970-01-01',
            'is_boolean': False,
        }

        # save
        with open('pickle.tmp', 'wb') as f:
            pickle.dump(data, f)

        self.assertTrue(os.path.isfile('pickle.tmp'))

        # load
        data = None
        with open('pickle.tmp', 'rb') as f:
            data = pickle.load(f)
            
        self.assertEqual('1970-01-01', data['bday'])
        self.assertEqual(4, len(data))

    def testInMemory(self):
        # save
        data = { 'first_name': 'Max' }
        buffer = pickle.dumps(data)

        self.assertIsInstance(buffer, bytes)

        # load
        data2 = pickle.loads(buffer)

        self.assertTrue(data == data2)
        self.assertFalse(data is data2)

