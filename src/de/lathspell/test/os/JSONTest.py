import unittest
import json

class JSONTestTest(unittest.TestCase):
    """
    Es gibt die Möglichkeit bei json.dump einen eigenen Serializer anzugeben
    mit dem dann auch Byte-Arrays und spezielle Objekte serialisiert werden
    können.
    """

    def testJSONTest(self):

        # save
        data = { 'first_name': 'Max', 'gf': None }
        buffer = json.dumps(data)

        self.assertIsInstance(buffer, str)
        self.assertEqual('{"gf": null, "first_name": "Max"}', buffer)

        # load
        data2 = json.loads(buffer)

        self.assertTrue(data == data2)
        self.assertFalse(data is data2)
