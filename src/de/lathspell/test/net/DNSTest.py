import unittest
import DNS

class DNSTestCase(unittest.TestCase):

    def testLazy(self):
        x = DNS.lazy.mxlookup('lathspell.de')
        self.assertEqual([(10, "mail3av.westend.com")], x)

        x = DNS.revlookup("212.117.79.2")
        self.assertEqual("www2.westend.com", x)

        reqobj=DNS.Request(server='dns1.netcologne.de')
        x = reqobj.req("lathspell.de", qtype=DNS.Type.A)
        self.assertEqual("NOERROR", x.header['status'])
        self.assertEqual(1, x.header['aa']) # authoritative answer
        self.assertEqual(1, len(x.answers))
        self.assertEqual('212.117.79.2', x.answers[0]['data'])

if __name__ == '__main__':
    unittest.main()

