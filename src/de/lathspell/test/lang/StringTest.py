import unittest
import math
import re

class  StringTest(unittest.TestCase):

    def testString(self):
        s = "Täst"
        self.assertEqual(4, len(s))

    def testFormat(self):
        s = "This is {0} of {1}".format(3, "Foo")
        self.assertEqual("This is 3 of Foo", s)

        # Python 3.1+ Syntax
        s = "This is {} of {}".format(3, 'Foo')
        self.assertEqual("This is 3 of Foo", s)

        # Parameter können in verschiedenen Reihenfolgen stehen, praktisch für i18n
        s = "This is {2:-06.2f} of {4}".format(None, None, math.pi, None, "Foo")
        self.assertEqual("This is 003.14 of Foo", s)

        # Der Parameter kann aus einer Liste entnommen werden
        suffixes = ['KB', 'MB', 'GB', 'TB']
        s = "This is {0[2]}".format(suffixes)
        self.assertEqual("This is GB", s)

        # Runden? Nein, genauso wie printf(3)
        self.assertEqual("2", "{0:.0f}".format(2.5))

        # Justifying
        self.assertEqual('  7', "{:>3}".format(7))

    def testFunktionen(self):
        s = "Hello World"
        self.assertEqual("hello world", s.lower())

        # Anzahl der Buchstaben 'l' im String s
        self.assertEqual(3, s.count('l'))

    def testSlicing(self):
        s = "Hello World"
        self.assertEqual('Hello', s[0:5])

    def testRegex(self):
        s = "Hello World"

        self.assertEqual("Hallo World", s.replace('Hello', 'Hallo'))
        self.assertEqual("Hallo World", re.sub('^He..o', 'Hallo', s))

        # Matche starten, wie bei Java, am Zeilenanfang!
        self.assertTrue(re.match('.*\\sWor[^x]', s))
        # Statt dem Doppelbackslah geht auch dies:
        self.assertTrue(re.match(r'.*\sWor[^x]', s))

        # Gruppen finden; An Position 0 steht nicht der ganze String wie in PHP
        m = re.match(r'H(...)o (.*)$', s).groups()
        self.assertEqual(('ell', 'World'), m)

        
