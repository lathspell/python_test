import unittest
import urllib.request
from urllib.parse import urlencode
# from http.client import HTTPConnection
# HTTPConnection.debuglevel = 1

class HTTPTestTest(unittest.TestCase):
    """
    Sehr viel Bequemer soll die httplib2 sein, die allerdings nicht
    im Standard-Python dabei ist.
    """

    def testGET(self):
        url = 'http://www.google.de/'
        data_bytes = urllib.request.urlopen(url).read()
        data_str = str(data_bytes)

        self.assertTrue('Datenschutz' in data_str)

    def testHTTPConnection(self):
        response = urllib.request.urlopen('http://www.google.de/')
        header_strings = response.headers.as_string()
        self.assertTrue('Content-Type: text/html' in header_strings)

    def testUrlEncode(self):
        data = {'status': 'Test mit Python'}
        self.assertEqual('status=Test+mit+Python', urlencode(data))